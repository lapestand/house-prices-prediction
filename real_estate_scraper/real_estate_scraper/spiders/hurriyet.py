import re
import logging
import datetime
import scrapy
from ..items import RealEstateScraperItem
#from scrapy.utils.log import configure_logging
from scrapy.selector import Selector


class HurriyetSpider(scrapy.Spider):
    name = 'hurriyet_scraper'
    allowed_domains = ['hurriyetemlak.com']
    # start_urls = [f"https://www.hurriyetemlak.com/satilik/daire?page={idx}" for idx in range(1, 2)]
    page_template = "https://www.hurriyetemlak.com/satilik/daire?page={}"
    start_urls = ["https://www.hurriyetemlak.com/satilik/daire?page=1"]
    # start_urls = ["https://www.hurriyetemlak.com/satilik/daire?page=1"]
    
    trans_table = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")
    #    configure_logging(install_root_handler=False)
    #    logging.basicConfig(level=logging.WARNING, filename='err.log', filemode="a+", format='%(name)s - %(levelname)s - %(message)s')


    # start_urls = ["https://www.hurriyetemlak.com/satilik/daire?page=5865"]

    def parse(self, response):
        estate_urls = response.css("div.list-view-line a.img-link::attr(href)").getall()
        estate_count = len([response.urljoin(estate_url) for estate_url in estate_urls if self.allowed_domains[0] not in estate_url]) if estate_urls else 0
        

        print(f"Current page URL -> \"{response.request.url}\" && Estate count in this page -> {estate_count} | DATE TIME -> {str(datetime.datetime.now())}")

        if int(response.request.url.split('=')[-1]) < int(self.param_start):
            next_page = self.page_template.format(int(self.param_start))
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            if estate_urls:
                estate_urls = [response.urljoin(estate_url) for estate_url in estate_urls if self.allowed_domains[0] not in estate_url]

                for idx, estate_url in enumerate(estate_urls):
                    if "daire" in estate_url:
                        # print(f"\t\tCurrent Estate is {estate_url}\n")
                        yield scrapy.Request(estate_url, callback=self.parse_estate)
                


            next_page = response.xpath("//ul[@class=\"pagination\"]/li[@class=\"next-li pagi-nav\"]").get()
            
            if "disable" not in next_page:
                next_page = self.page_template.format(int(response.request.url.split('=')[-1]) + 1)
                if int(response.request.url.split('=')[-1]) + 1 < int(self.param_stop):
                    yield scrapy.Request(next_page, callback=self.parse)
        

    def parse_estate(self, response):
        features    = RealEstateScraperItem()
        
        short_info  = [inf.translate(self.trans_table).lower() for inf in response.css("ul.short-info-list li::text").getall()]
        adv_info    = [inf.translate(self.trans_table).lower() for inf in response.css("ul.adv-info-list li").getall()]

        detailed_info_xpath = "//section[@class=\"properties detail\"]/div[@class=\"properties-content det-block\"]/div[@class=\"properties-column\"]"
        price_xpath = "//p[@class=\"fontRB fz24 price\"]/text()"
        # print(short_info, end="\n" * 5)


        # features["address"] = ' '.join(short_info[:-2]).replace('\n', '')
        # features["address"] = ' '.join(short_info[:short_info.index("satilik")]).replace('\n', '')
        # print(' '.join(short_info[:-2]).replace('\n', ''))
        
        
        # print(' '.join(short_info[:3]).replace('\n', ''))
        adres = [_.strip() for _ in short_info[:3]]

        features["url"]     = response.request.url
        features["il"]      = adres[0]
        features["ilce"]    = adres[1]
        features["mahalle"] = adres[2]
        features["fiyat"]   = response.xpath(price_xpath).getall()[0].split()[0]
        # print(features["fiyat"])

        broken = False
        for feature in adv_info:
            feature = Selector(text=feature).xpath("//span/text()").getall()
            # print(feature)
            try: 
                self.add_to_items(features, feature)
            except KeyError as e:
                broken
                logging.warning("\t\t->URL->\t".join([e, response.request.url]))
                # print(f"Unexpected feature \t\t ---> \t\t {feature_name}")

        for detailed_infos in response.xpath(detailed_info_xpath).getall():
            for detail in Selector(text=detailed_infos).xpath("//li/text()").getall():
                features[self.name_of(detail.strip())] = True

        #for k, v in features.items():
        #   print(f"{k}\t->\t{v}")
        if not broken:
            yield features

    def name_of(self, feature):
        t = str.maketrans("-'/ ", "____")
        feature = ' '.join(feature.split())
        return feature.translate(self.trans_table).lower().translate(t)
    

    def add_to_items(self, features, new_feature):
        feature_name = self.name_of(new_feature[0])
        try:
            if "oda + salon sayisi" in new_feature[0]:
                features["oda_sayisi"]   = ' '.join(new_feature[1:]).split('+')[0].strip()
                features["salon_sayisi"] = ' '.join(new_feature[1:]).split('+')[1].strip()
            elif "brut / net m2" in new_feature[0]:
                features["brut_m2"] = new_feature[1].strip("m2 /")
                features["net_m2"]  = new_feature[2].strip("m2 /")
            elif "cephe" in new_feature[0]:
                features[feature_name] = ''.join(new_feature[1:])
            else:
                if "fiyat" not in feature_name:
                    features[feature_name] = ' '.join(re.sub(r'\([^)]*\)', '', new_feature[1:][0]).split()).replace(". kat", '').replace(" yasinda", '') if isinstance(new_feature, list) and len(new_feature) > 1 else None
        except KeyError as e:
            raise KeyError(e)

"""
        print("\t\tOda + Salon: ", index_of("oda + salon sayisi", adv_info) + 1)
        print("\t\tBrüt / Net m2: ", index_of("brut / net m2", adv_info) + 1)
        print("\t\tBulundugu kat: ", index_of("bulundugu kat", adv_info) + 1)
"""

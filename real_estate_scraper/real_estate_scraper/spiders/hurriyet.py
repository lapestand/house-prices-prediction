import scrapy
from ..items import RealEstateScraperItem
from scrapy.selector import Selector


class HurriyetSpider(scrapy.Spider):
    name = 'hurriyet_scraper'
    allowed_domains = ['hurriyetemlak.com']
    # start_urls = [f"https://www.hurriyetemlak.com/satilik/daire?page={idx}" for idx in range(1, 2)]
    page_template = "https://www.hurriyetemlak.com/satilik/daire?page={}"
    start_urls = [page_template.format(1)]
    trans_table = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")

    # start_urls = ["https://www.hurriyetemlak.com/satilik/daire?page=5865"]

    def parse(self, response):
        print("CURRENT PAGE IS \"", response.request.url, "\"")
        estate_urls = response.css("div.list-view-line a.img-link::attr(href)").getall()
        if estate_urls:
            estate_urls = [response.urljoin(estate_url) for estate_url in estate_urls if
                           self.allowed_domains[0] not in estate_url]

            for idx, estate_url in enumerate(estate_urls):
                if "daire" in estate_url and idx == 0:
                    yield scrapy.Request(estate_url, callback=self.parse_estate)

            next_page = self.page_template.format(int(response.request.url.split('=')[-1]) + 1)
            if int(next_page[-1]) < 5:
                yield scrapy.Request(next_page, callback=self.parse)

    def parse_estate(self, response):
        def index_of(val, arr):
            try:
                return arr.index(val)
            except ValueError:
                return -1

        features = RealEstateScraperItem()
        short_info = [inf.translate(self.trans_table).lower() for inf in
                      response.css("ul.short-info-list li::text").getall()]
        adv_info = [inf.translate(self.trans_table).lower() for inf in
                    response.css("ul.adv-info-list li").getall()]

        detailed_info_xpath = "//section[@class=\"properties detail\"]/div[@class=\"properties-content " \
                              "det-block\"]/div[@class=\"properties-column\"]"

        print(short_info, end="\n" * 5)
        # adv_info.insert(0, None)
        print(adv_info)

        print("\t Estate -> \"", response.request.url, "\"")

        print("\t\tAddres: ", ' '.join(short_info[:-2]).replace('\n', ''))
        for feature in adv_info:
            print(feature)
            feature_name = feature[54:feature.index("</span>")]
            print('\t' + feature_name)
            feature = feature[feature.index("</span>") + len("</span>"):].strip()
            # if feature.startswith("<div"):
            print('\t' + feature)
            # print(f"\t\t{adv_info[index_of(feature, adv_info)]}: {adv_info[index_of(feature, adv_info) + 1]}")

"""
        print("\t\tOda + Salon: ", index_of("oda + salon sayisi", adv_info) + 1)
        print("\t\tBrüt / Net m2: ", index_of("brut / net m2", adv_info) + 1)
        print("\t\tBulundugu kat: ", index_of("bulundugu kat", adv_info) + 1)
"""

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import RealEstateScraperItem


class HurriyetSpider(CrawlSpider):
    name = 'hurriyet_scraper'
    allowed_domains = ['hurriyetemlak.com']
    max_page = 5840
    start_urls = [f"https://www.hurriyetemlak.com/satilik/daire?page={idx}" for idx in range(1, 10)]

    def parse_(self, response):
        features = RealEstateScraperItem()
        links = response.css("div.list-view-line a.img-link::attr(href)").getall()
        base_url = "www.hurriyetemlak.com"

        links = [response.urljoin(link) for link in links if base_url not in link]
        for idx, link in enumerate(links):
            features['url'] = link

        yield {
            "links": links,
        }

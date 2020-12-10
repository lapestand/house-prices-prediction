import scrapy


class SahibindenScraperSpider(scrapy.Spider):
    name = 'sahibinden_scraper'
    allowed_domains = ['sahibinden.com']
    max_quarter = 67593
    start_urls = [f"https://www.sahibinden.com/satilik-daire?address_quarter={idx}" for idx in range(max_quarter)]
    download_delay = 1.0

    def parse(self, response):
        page_count = response.xpath("/html/body/div[4]/div[4]/form/div/div[3]/div[1]/div[2]/div[1]/div[1]/span").get()
        print(page_count)

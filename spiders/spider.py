from scrapy.spiders import Spider
from qixiu.items import CarItem
from scrapy import Request

class CarSpider(Spider):
    name = 'car'
    start_urls = ['http://www.gzweix.com/article/sort0253/sort0254/list254_1.html']
    base_url = 'http://www.gzweix.com'
    def parse(self, response):
        item = CarItem()
        # 第一层
        brands = response.xpath('//div[@id="mainBody6"]//span[@class="boxhead"]/a/text()').extract()
        brands_url = response.xpath('//div[@id="mainBody6"]//span[@class="boxhead"]/a/@href').extract()

        # 第二层
        car_titles = response.xpath('//ul[@id="mainlistUL5"]/li[@class="mainlist_li5"]/span[@class="list_title5"]/a/text()').extract()
        car_url =  response.xpath('//ul[@id="mainlistUL5"]/li[@class="mainlist_li5"]/span[@class="list_title5"]/a/@href').extract()
        if brands:
            for brand in brands:
                item['brand'] = brand
                yield item
        if car_titles:
            for car_title in car_titles:
                item['car_title'] = car_title
                yield item
        if brands_url:
            for index, brand_url in enumerate(brands_url):
                type_url = type(brand_url)
                cars_url = self.base_url + brand_url
                yield Request(cars_url)
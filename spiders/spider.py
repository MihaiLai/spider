from scrapy.spiders import Spider
from qixiu.items import CarItem

class CarSpider(Spider):
    name = 'car'
    start_urls = ['http://www.gzweix.com/article/sort0253/sort0254/list254_1.html']

    def parse(self, response):
        item = CarItem()
        titles = response.xpath('//span[@class="boxhead"]/a/text()').extract()
        for title in titles:
            item['brand'] = title
            yield  item
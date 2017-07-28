from scrapy.spiders import Spider
from qixiu.items import CarItem
from scrapy import Request
import math
import re

class CarSpider(Spider):
    name = 'car'
    start_urls = ['http://www.gzweix.com/article/sort0253/sort0254/list254_1.html']
    base_url = 'http://www.gzweix.com'
    cars_url = ''
    def parse(self, response):
        item = CarItem()
        # 第一层
        brands = response.xpath('//div[@id="mainBody6"]//span[@class="boxhead"]/a/text()').extract()
        brands_url = response.xpath('//div[@id="mainBody6"]//span[@class="boxhead"]/a/@href').extract()

        # 第二层
        car_titles = response.xpath('//ul[@id="mainlistUL5"]/li[@class="mainlist_li5"]/span[@class="list_title5"]/a/text()').extract()
        car_url = response.xpath('//ul[@id="mainlistUL5"]/li[@class="mainlist_li5"]/span[@class="list_title5"]/a/@href').extract()



        if brands:
            for brand in brands:
                item['brand'] = brand
                yield item
        if car_titles:
            for car_title in car_titles:
                item['car_title'] = car_title
                yield item
        if brands_url:
            self.cars_url = self.base_url + brands_url[0]
            #this_page = int(re.search(r'list\d+_(\d+)', cars_url).group(1))
            yield Request(self.cars_url)


        # car 下一页
        car_article_nums = response.xpath('//div[@class="mainNextPage5"]/var[@class="morePage"]/b[1]/text()').extract()
        car_article_num = 0
        if car_article_nums:
            car_article_num = math.ceil(float(car_article_nums[0][3:])/30)
            if car_article_num > 1:
                for i in range(2, car_article_num+1):
                    page = '_' + str(i)
                    this_url = response.url
                    next_cars_url = re.sub(r'_\d+', page, this_url)
                    if next_cars_url:
                        yield Request(next_cars_url)



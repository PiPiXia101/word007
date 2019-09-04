# -*- coding: utf-8 -*-
import json
from scrapy.http import Request, FormRequest
import scrapy
from fake_useragent import UserAgent
from ..items import Word007Item


class WordSpider(scrapy.Spider):
    name = 'words'
    allowed_domains = ['www.word007.com']
    url_1 = 'https://www.word007.com/studycenter/elective/tm'
    url_2 = 'https://www.word007.com/studycenter/bookstudy'
    url_3 = 'https://www.word007.com/studycenter/wordsstudy/list'

    def start_requests(self):
        url = 'https://www.word007.com/studycenter/elective/tmv'
        my_data = {'typeId': '0'}
        yield scrapy.FormRequest(
            url=url,
            formdata=my_data,
        )

    def parse(self, response):
        # result = json.loads(response.text)
        # for item in result:
        #     versionId = item['id']
        #     url = 'https://www.word007.com/studycenter/elective/tm'
        #     formdata = {
        #         'versionId': str(versionId),
        #         'pageNum': '1',
        #         'pageSize': '8'
        #     }
        #     yield scrapy.FormRequest(
        #         url=url,
        #         formdata=formdata,
        #         callback=self.parse_2
        #     )

        formdata = {
            'versionId': '68',
            'pageNum': '1',
            'pageSize': '8'
        }
        yield scrapy.FormRequest(
            url=self.url_1,
            formdata=formdata,
            callback=self.parse_2
        )

    def parse_2(self, response):
        # result = json.loads(response.text)
        # list = result['list']
        #
        # for item in list:
        #     id = item['id']
        #     name = item['bookName']
        #     formdata = {
        #         'id': str(id),
        #         'bookName': name
        #     }
        #     yield scrapy.FormRequest(
        #         url=self.url_1,
        #         formdata=formdata,
        #         callback=self.parse_3
        #     )
        formdata = {
            'id': '329',
            'bookName': '小升初分类词汇 1'
        }
        yield scrapy.FormRequest(
            url=self.url_2,
            formdata=formdata,
            callback=self.parse_3
        )

    def parse_3(self, response):
        # hashBookId = response.xpath("//span[@id='intelligentDictationBtn']/@data-hash-book-id").get()
        # unites = response.xpath("//div[@data-unit-id]")
        # for unit in unites:
        #     unitId = unit.xpath("./@data-unit-id").get()
        #     formdata = {
        #         'hashBookId':str(hashBookId),
        #         'unitId':str(unitId)
        #     }
        #     yield scrapy.FormRequest(
        #         url=self.url_3,
        #         formdata=formdata,
        #         callback=self.parse_4
        #     )
        formdata = {
            'hashBookId': 'dcda0a027b48a2df3ada7218f9da076b',
            'unitId': '3407'
        }
        yield scrapy.FormRequest(
            url=self.url_3,
            formdata=formdata,
            callback=self.parse_4
        )

    def parse_4(self, response):
        result = json.loads(response.text)
        words = result['data']['list']
        item = Word007Item()
        item['words'] = words
        yield item


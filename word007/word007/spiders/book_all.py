# -*- coding: utf-8 -*-
import json
from scrapy.http import Request, FormRequest
import scrapy
from fake_useragent import UserAgent
from ..items import Word007Item


class WordSpider(scrapy.Spider):
    name = 'word'
    allowed_domains = ['www.word007.com']

    def start_requests(self):
        url = 'https://www.word007.com/studycenter/elective/tmv'
        my_data = {'typeId': '0'}
        yield scrapy.FormRequest(
            url=url,
            formdata=my_data,
        )

    def parse(self, response):
        result = json.loads(response.text)
        for item in result:
            book = Word007Item()
            book['book_id'] = item['id']
            book['book_name'] = item['versionName']
            yield book

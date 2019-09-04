# -*- coding: utf-8 -*-
import json

import scrapy

from ..items import Word007Item


class BookSortSpider(scrapy.Spider):
    name = 'book_sort'
    allowed_domains = ['www.word.com']

    # start_urls = ['http://www.word.com/']
    def start_requests(self):
        url = 'https://www.word007.com/studycenter/elective'
        yield scrapy.FormRequest(
            url=url,
            method='POST'
        )

    def parse(self, response):
        a_list = response.xpath("//a[@class='book-type']")
        for a in a_list:
            id = a.xpath('./@data-id').get()
            name = a.xpath('./text()').get()

            yield scrapy.FormRequest(
                url='https://www.word007.com/studycenter/elective/tmv',
                # 把item传递到下一个解析函数
                formdata={
                    'typeId': id
                },
                meta={'id': id, 'name': name},
                callback=self.get_book_sort,
                dont_filter=True
            )

    def get_book_sort(self, response):
        book = Word007Item()
        id = response.meta['id']
        name = response.meta['name']
        result = json.loads(response.text)
        book_sorts = {
            'sid': id,
            'sname': name,
            'bookes': []
        }
        for item in result:
            book_sort = {}
            book_sort['bid'] = item['id']
            book_sort['bname'] = item['versionName']
            book_sorts['bookes'].append(book_sort)

        book['book_sorts'] = book_sorts
        yield book

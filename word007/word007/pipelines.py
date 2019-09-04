# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import os

import scrapy
from scrapy.pipelines.images import ImagesPipeline
import tesserocr
from PIL import Image


class Word007PipelineBookAll(object):
    def process_item(self, item, spider):
        print(item['book_id'], item['book_name'])
        return item


class Word007PipelineBookSort(object):
    def process_item(self, item, spider):
        print(item['book_sorts'])
        return item

class Word007PipelineWords(object):
    def process_item(self, item, spider):
        print(item['words'])
        return item


class JsonWithEncodingPipeline(object):
    def __init__(self):
        # 修改文件名
        self.file = codecs.open('bookAll.json', 'w', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line + ',')
        return item

    def close_spider(self, spider):
        self.file.seek(-1, os.SEEK_END)
        self.file.truncate()
        self.file.write(']')
        self.file.close()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import json
# import codecs
from scrapy.exporters import JsonItemExporter


class BrowsewaveTaskPipeline(object):
    def process_item(self, item, spider):
        return item

# class JsonWithEncodingPipeline(object):
#
#     def __init__(self):
#         self.file = codecs.open('products_through_pipeline.jl', 'w', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.file.write(line)
#         return item
#
#     def spider_closed(self, spider):
#         self.file.close()


class JsonWithEncoding2Pipeline(object):

    def __init__(self):
        self.file = open("products_through_pipeline2.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

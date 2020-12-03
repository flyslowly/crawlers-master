# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient

class AutohomecrawlerPipeline:
    def __init__(self):
        self.connection = MongoClient('localhost', 27017)
        self.db = self.connection.autohome
        self.forum = self.db.forum
        self.qa = self.db.qa
        self.article = self.db.article

    def process_item(self, item, spider):
        if not self.forum or not item:
            return
        self.forum.save(item)
        return item

    def __del__(self):
        if self.forum:
            self.forum.close()
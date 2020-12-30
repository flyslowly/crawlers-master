# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from items import ForumItem
from settings import MONGO_URI

class AutohomecrawlerPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.client = None
        self.db= None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=MONGO_URI,
            mongo_db='autohome',
        )
    
    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()


    def process_item(self, item, spider):
        if isinstance(item, ForumItem):
            self._process_forum(item)
        # elif isinstance(item, ZhihuRelationItem):
        #     self._process_relation(item)
        return item

    def _process_forum(self, item):
        collection = self.db['forum']
        # collection.save(dict(item))
        collection.save(item)

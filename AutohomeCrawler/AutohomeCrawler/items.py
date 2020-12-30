# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutohomecrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    forum_content = scrapy.Field()
    forum_comment = scrapy.Field()
    forum_username = scrapy.Field()
    forum_link = scrapy.Field()


class ForumItem(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()
    comment = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()
    post_date = scrapy.Field()
    description = scrapy.Field()
    reply = scrapy.Field()
    _id = scrapy.Field()

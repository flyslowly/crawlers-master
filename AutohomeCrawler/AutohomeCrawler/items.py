# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ForumItem(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field() #内容
    comment = scrapy.Field() #评论
    title = scrapy.Field() #标题
    source = scrapy.Field() #论坛名
    post_date = scrapy.Field() #发表日期
    description = scrapy.Field() #图片描述
    reply = scrapy.Field() #评论的回复
    # _id = scrapy.Field()

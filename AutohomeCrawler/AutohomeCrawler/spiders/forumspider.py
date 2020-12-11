# -*- coding: utf-8 -*-
import scrapy
from AutohomeCrawler.items import ForumSpiderItem
from .parsefont import ParseFont
import re
import uuid


class ForumSpider(scrapy.Spider):
    meta_no_redirect = {
        'handle_httpstatus_list': [302, 404]
    }
    name = 'forumspider'
    start_urls = [
        'https://sou.autohome.com.cn/luntan?q=OTA%C9%FD%BC%B6&pvareaid=100834&page=1&entry=44',
    ]

    def _parse(self, response):

        forum_content_list = response.xpath('//*[@id="content"]/div[1]/div[2]/div/dl')
        for content in forum_content_list:
            content_link = content.xpath('./dt/a').attrib['href']
            print(content_link)
            yield response.follow(content_link, self.parse_content)

        # next_page = response.xpath('//*[@id="content"]/div[1]/div[5]/a[@class="page-item-next"]').attrib['href']
        # if next_page is not None:
        #     next_page = self.start_urls[0].split('?')[0] + next_page
        #     yield response.follow(next_page, self._parse)

    def parse_content(self, response):
        if response.xpath('//h1[@class="post-delete-title"]/text()').get() == '主楼已被删除':
            return
        if response.xpath('//*[@id="videoWrap"]'):
            return

        source = response.xpath('//*[@id="js-sticky-toolbar"]//a[@class="name"]/text()').get()
        title = response.xpath('//*[@id="js-sticky-toolbar"]//div[@class="toolbar-left-title"]/a/text()').get()
        post_date = response.xpath('//span[@class="post-handle-publish"]/strong/text()').get().split(" ")[0]

        content_list = response.xpath("//div[@class='tz-paragraph']//text()").getall()
        descriptions = response.xpath("//div[@class='description']//text()").getall()

        comments = response.xpath('//div[@class="reply"]//div[@class="reply-detail"]//text()').getall()

        replys = response.xpath('//div[@class="reply"]//div[@class="reply-sub-cont"]//text()').getall()

        content = ''
        for elem in content_list:
            content += elem

        # 对图片的描述
        description = ''
        for elem in descriptions:
            description += elem

        for i in range(len(comments)):
            comments[i] = comments[i].replace('\n', '').strip()
        list(filter(None, comments))

        comment = ''
        for elem in comments:
            content += elem

        for i in range(len(replys)):
            replys[i] = replys[i].replace('\n', '').strip()
        list(filter(None, replys))

        reply = ''
        for elem in replys:
            reply += elem

        cmp = re.compile(r",url\('(\/\/.*.ttf)'\).*?\('woff'\)")
        font_url = cmp.findall(response.text)[0]
        font_dict = ParseFont(font_url).parse_font()
        for key, value in font_dict.items():
            content.replace(key, value)
            description.replace(key, value)
            comment.replace(key, value)
            reply.replace(key, value)

        item = ForumSpiderItem()
        item['source'] = source
        item['title'] = title
        item['post_date'] = post_date
        item['content'] = content
        item['description'] = description
        item['comment'] = comment
        item['reply'] = reply
        item['_id'] = uuid.uuid1()
        yield item

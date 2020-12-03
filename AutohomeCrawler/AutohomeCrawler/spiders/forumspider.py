# -*- coding: utf-8 -*-
import scrapy
from AutohomeCrawler.items import ForumSpiderItem


class ForumSpider(scrapy.Spider):
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

        next_page = response.xpath('//*[@id="content"]/div[1]/div[5]/a[@class="page-item-next"]').attrib['href']
        if next_page is not None:
            next_page = self.start_urls[0].split('?')[0] + next_page
            yield response.follow(next_page, self._parse)

    def parse_content(self, response):
        if response.xpath('//h1[@class="post-delete-title"]/text()').get() == '主楼已被删除':
            return
        if response.xpath('/html/body/comment()[11]').extract()[0].split(' ')[1] == '视频':
            return

        source = response.xpath('//*[@id="js-sticky-toolbar"]//a[@class="name"]/text()').get()
        title = response.xpath('//*[@id="js-sticky-toolbar"]//div[@class="toolbar-left-title"]/a/text()').get()
        post_date = response.xpath('//span[@class="post-handle-publish"]/strong/text()').get().split(" ")[0]

        content_all = response.xpath('//*[@id="content"]/div[1]/div[2]/div')
        content_list = content_all.xpath('./dl')
        for content in content_list:
            item = ForumSpiderItem()
            item['link'] = content.xpath('./a').attrib['href'],
            item['title'] = content.xpath('./a').attrib['data-title'],
            item['source'] = content.xpath('./dd[2]/span[1]/text()').get().split('：')[1],
            item['post_date'] = content.xpath('./dd[2]/span[3]/text()').get().split('：')[1]
            yield item

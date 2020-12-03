import scrapy

class QiushiSpider(scrapy.Spider):
    name = 'qiushibaike'
    def start_requests(self):
        urls = [
            'https://www.qiushibaike.com/text/page/1/',
            'https://www.qiushibaike.com/text/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        content_left_div = response.xpath('//*[@class="col1 old-style-col1"]')
        content_list_div = content_left_div.xpath('./div')

        for content_div in content_list_div:
            yield {
                'author': content_div.xpath('./div/a[2]/h2/text()').get(),
                'content': content_div.xpath('./a/div/span/text()').getall(),
            }
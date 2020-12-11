# -*- coding: utf-8 -*-
from fontTools.ttLib import TTFont
import requests
import re
from lxml import etree
import os


class ParseFont:
    def __init__(self, font_url):
        self.font_url = font_url
        self.parse_font()

    def parse_font(self):
        # old_font = TTFont(r'./fonts/ChcCQ1sUz2iATgrtAABj9DiBxVE68..ttf')
        old_font = TTFont(r'./AutohomeCrawler/spiders/fonts/ChcCQ1sUz2iATgrtAABj9DiBxVE68..ttf')
        font_file = self.download_font(self.font_url)
        font_file_name = self.font_url.split('/')[-1]
        with open('AutohomeCrawler/spiders/fonts/' + font_file_name, 'wb') as f:
            f.write(font_file)

        new_font = TTFont(r'./AutohomeCrawler/spiders/fonts/' + font_file_name)

        # with open('fonts/' + font_file_name, 'wb') as f:
        #     f.write(font_file)
        #
        # new_font = TTFont(r'./fonts/' + font_file_name)

        old_word_list = ['着', '和', '上', '不', '二', '低', '六', '五', '矮', '很', '远', '右', '多', '坏', '少', '好', '十', '小',
                         '九', '八', '了', '长', '得', '下', '七', '四', '地', '左', '三', '更', '高', '近', '的', '呢', '短', '是',
                         '一', '大']
        old_unicode_list = ['uniED1D', 'uniED6F', 'uniECBC', 'uniEDFC', 'uniEC5A', 'uniED9B', 'uniEDEC', 'uniED39',
                            'uniEC86',
                            'uniECD7', 'uniEC24', 'uniED65', 'uniEDB6', 'uniED03', 'uniED55', 'uniECA1', 'uniEDE2',
                            'uniEC40',
                            'uniED80', 'uniECCD', 'uniED1F', 'uniEC6B', 'uniECBD', 'uniEDFE', 'uniED4A', 'uniED9C',
                            'uniECE9',
                            'uniEC35', 'uniEC87', 'uniEDC8', 'uniEC26', 'uniED66', 'uniECB3', 'uniED05', 'uniEC51',
                            'uniED92',
                            'uniEDE4', 'uniED30']
        new_unicode_list = new_font.getGlyphNames()[1:]
        old_word_dict = dict(zip(old_unicode_list, old_word_list))

        old_coordinate_list = []
        for unicode in old_unicode_list:
            coordinate = old_font['glyf'][unicode].coordinates
            old_coordinate_list.append(list(coordinate))

        new_coordinate_list = []
        for unicode in new_unicode_list:
            coordinate = new_font['glyf'][unicode].coordinates
            new_coordinate_list.append(list(coordinate))

        i = -1
        new_word_dict = {}
        for new_unicode in new_coordinate_list:
            i += 1
            j = -1
            for old_unicode in old_coordinate_list:
                j += 1
                if self.compare(old_unicode, new_unicode):
                    new_word_dict[new_unicode_list[i]] = old_word_dict[old_unicode_list[j]]

        # print(new_word_dict)
        new_word_dict_unicode = {eval("u'\\u" + key[3:].lower() + "'") : value for key, value in new_word_dict.items()}
        # print(new_word_dict_unicode)

        # os.remove(r'./fonts/' + font_file_name)
        os.remove(r'./AutohomeCrawler/spiders/fonts/' + font_file_name)

        return new_word_dict_unicode

    def download_font(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/'
                          '537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        try:
            res = requests.get('http:' + url, headers=headers)
            if res.status_code == 200:
                return res.content
        except requests.RequestException:
            print('下载字体失败...')
            return None

    def compare(self, c1, c2):
        """
        :param c1: coordinates list of first word
        :param c2: coordinates list of second word
        :return: True when deviation is <50
        """
        if len(c1) != len(c2):
            return False
        else:
            for i in range(len(c1)):
                if abs(c1[i][0] - c2[i][0]) < 50 and abs(c1[i][1] - c2[i][1]) < 50:
                    pass
                else:
                    return False
            return True


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/'
                      '537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    baseurl = '//k3.autoimg.cn/g1/M09/D2/CF/ChcCQ1sUz16AbTQfAABj6MxuvgQ78..ttf'
    url = 'https://club.autohome.com.cn/bbs/thread/7216298b897a1f6e/92261941-1.html'
    response = requests.get(url=url, headers=headers)
    page = etree.HTML(response.text)
    source = page.xpath('//*[@id="js-sticky-toolbar"]//a[@class="name"]/text()')[0]
    title = page.xpath('//*[@id="js-sticky-toolbar"]//div[@class="toolbar-left-title"]/a/text()')[0]
    post_date = page.xpath('//span[@class="post-handle-publish"]/strong/text()')[0].split(" ")[0]

    content_list = page.xpath("//div[@class='tz-paragraph']//text()")
    descriptions = page.xpath("//div[@class='description']//text()")



    cmp = re.compile(r",url\('(\/\/.*.ttf)'\).*?\('woff'\)")
    font_url = cmp.findall(response.text)[0]
    font_dict = ParseFont(font_url).parse_font()
    # s_font_dict = {key.replace('uni', u'\\u') : value for key, value in font_dict.items()}
    # s_font_dict = {eval("u'\\u" + key[3:] + "'") : value for key, value in font_dict.items()}

    # print(s_font_dict)

    content = ''
    for elem in content_list:
        # for key, value in s_font_dict.items():
        #     elem = elem.replace(key, value)
        content += elem

    # 对图片的描述
    description = ''
    for elem in descriptions:
        # for key, value in s_font_dict.items():
        #     elem = elem.replace(key, value)
        description += elem
    # for key in font_dict.keys():
    #     changed_key = r"u'\u" + key[3:] + "'"
    #     s_font_dict[changed_key] = font_dict[key]

    # s_font_dict = [eval(r"'&#x" + key[3:].lower() + "'") for key in font_dict]
    # word_list = []
    #
    # for value in font_dict.values():
    #     word_list.append(value)

    # ss_font_dict = dict(zip(s_font_dict, word_list))
    # for key in font_dict:
    #     change_key = r'\u' + key[3:] +';'
    #     s_font_dict[change_key.decode('unicode_escape')] = font_dict[key]
    for key,value in font_dict.items():
        content = content.replace(key , value)
        description = description.replace(key , value)

    print('source: ' + source)
    print('title: ' + title)
    print('post_date: ' + post_date)
    print('content: ' + content)
    print('description: ' + description)

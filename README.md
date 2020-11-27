# crawlers-master
## Car forums
### International forums
- https://www.speakev.com/search/514139/?q=ota&o=date

### Local forums
- 汽车之家： 口碑页， 论坛页
- 懂车帝 all from 今日头条 but has own comments
- 虎扑-汽车交友论坛
- 爱卡汽车
- 易车

## 学习网址
[跟着小帅b玩Python爬虫](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU2ODYzNTkwMg==&action=getalbum&album_id=1321044729160859650&scene=173&from_msgid=2247484386&from_itemidx=1&count=3#wechat_redirect)

### urllib
```
urllib.request.urlopen(url, data=None, [timeout, ]*)

urllib.request.Request(url, data=None, headers={}, method=None)
```

```python

from urllib import request, parse
import ssl

context = ssl._create_unverified_context()

url = 'https://biihu.cc//account/ajax/login_process/'
headers = {
    # 假装自己是浏览器
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/71.0.3578.98 Safari/537.36',
}

diction = {
    'return_url': 'https://biihu.cc/',
    'user_name': 'xiaoshuaib@gmail.com',
    'password': '123456789',
    '_post_type': 'ajax',
}

data = bytes(parse.urlencode(diction), 'utf-8')

req = request.Request(url, data=data, headers=headers, method='POST')

response = request.urlopen(req, context=context)

print(response.read().decode('UTF-8'))

```


### requests
[Requests](https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484115&idx=1&sn=4f9ca3f0938cf9d9eaa9c6ff6c457481&chksm=fc8bba42cbfc335478f72ef83049238aab250f5cf471cffe60b9ac736368b0eb4dbd2c74bcfd&cur_album_id=1321044729160859650&scene=189#rd)

#### 不同请求
=======
```python
>>> r = requests.get('https://api.github.com/events')

>>> r = requests.post('https://httpbin.org/post', data = {'key':'value'})

>>> r = requests.put('https://httpbin.org/put', data = {'key':'value'})

>>> r = requests.delete('https://httpbin.org/delete')

>>> r = requests.head('https://httpbin.org/get')

>>> r = requests.options('https://httpbin.org/get')
```

#### 带参数
=====
```pyhon
>>> payload = {'key1': 'value1', 'key2': 'value2'}

>>> r = requests.get('https://httpbin.org/get', params=payload)
```

#### 伪装浏览器
=========
```python
>>> url = 'https://api.github.com/some/endpoint'

>>> headers = {'user-agent': 'my-app/0.0.1'}

>>> r = requests.get(url, headers=headers)
```

### 正则
`import re`

[regular expression](https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484120&idx=1&sn=5f5a2ad4f9c458c4ed04c2726cf0b6f2&chksm=fc8bba49cbfc335f1dae0ffc2ad03cad443cb944c2666ba51f70e0e9663bb86bc960971bf804&cur_album_id=1321044729160859650&scene=189#rd)

```
re.match
re.search
re.findall
re.sub
re.compile
```

### BeautifulSoup
```
soup = BeautifulSoup(html_doc,'lxml')
print(soup.title.string)
print(soup.p.string)
print(soup.title.parent.name)
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id="link2"))
print(soup.get_text())
```

### CSS select for soup
```
soup = BeautifulSoup(html_doc,'lxml')

print(soup.select("title"))
print(soup.select("body a"))
print(soup.select("p > #link1"))
```


### Selenium
- pip install selenium
[download driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
config PATH
restart IDE

[link](https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484164&idx=1&sn=174af324601e22f9809f058760233121&chksm=fc8bbb95cbfc328356c4c7358ef4d25146ac382660dd2a91efe8e132ef4364dab9aa9ef8069a&cur_album_id=1321044729160859650&scene=189#rd)

```
driver = webdriver.Chrome()

- find_element_by_id

- find_element_by_name

- find_element_by_xpath

- find_element_by_link_text

- find_element_by_partial_link_text

- find_element_by_tag_name

- find_element_by_class_name

- find_element_by_css_selector
```

if more elements use '**elements**' instead of '**element**'

```
driver.find_elements(By.ID, 'xxx')
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

driver.current_url
driver.get_cookies()
driver.page_source
input.text
```

### JSON
Python object to JSON
`json.dumps()`

JSON to python object
`json.loads()`

### 多线程与多进程
并行：在某一个时间段里，可以同时执行多个进程
并发：就是在一个时间点，同时执行多个进程
threading.Thread  multiprocession.dummy
#### 互斥锁
GIL锁：控制线程执行权限

#### 协程
so called 微线程
genvent mnkey.patch_all

#### 多线程
module: _thread, threading, Queues
Usually use threading

在 python 中  可以使用 ThreadPoolExecutor() 来实现线程池
#### Queue
有点复杂

#### 多进程
```
from multiprocessing import Process
from multiprocessing import Pool
```

### 代理ip池
[Link](https://github.com/Python3WebSpider/ProxyPool)

### 模拟登录
#### 三种登录方法
- Cookie
- 发送表单，urllib
- Selenium
    - 拿到输入框的selector，登录后webdriver.get_cookies()拿到cookie

#### 验证码
[Link](https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484292&idx=1&sn=1d948f56e57a6586f11aabc0f0f6b3af&chksm=fc8bbb15cbfc3203d94db31655c19a069625bd0d697fc9ce9f4633d336086ba17f675fcad19f&cur_album_id=1321044729160859650&scene=189#rd)
tool： Python-tesseract
pip install pytesseract
安装 tesseract-ocr

```python
pytesseract.image_to_string()
//#处理灰度
img.convert('L') 
// 二值化
def convert_img(img,threshold):
    img = img.convert("L")  # 处理灰度
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img
//降噪
data = img.getdata()
    w,h = img.size
    count = 0
    for x in range(1,h-1):
        for y in range(1, h - 1):
            # 找出各个像素方向
            mid_pixel = data[w * y + x]
            if mid_pixel == 0:
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                down_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]

                if top_pixel == 0:
                    count += 1
                if left_pixel == 0:
                    count += 1
                if down_pixel == 0:
                    count += 1
                if right_pixel == 0:
                    count += 1
                if count > 4:
                    img.putpixel((x, y), 0)
```


#### 滑动识别
[Link](https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484321&idx=1&sn=4bc73324acfacda7d3bc82120b19d11a&chksm=fc8bbb30cbfc322656122f7e2d88eb509a50a3a71e89d9892f73115823b55242eb3be586f1b0&cur_album_id=1321044729160859650&scene=189#rd)

#### 模拟登录模型脚本
[Link](https://github.com/CriseLYJ/awesome-python-login-model)

### Appnium
爬取手机app数据


### 数据存储
#### CSV
库：
- csv
    - import csv
- pandas
    - pip install pandas

#### MySQL
[Link](https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484510&idx=1&sn=316cec6eab70fcd8005cc580a66e02aa&chksm=fc8bbccfcbfc35d9cea2ec45e3138918596c37fdb3e0ced2d88c077d63cf5ed29842358a5896&cur_album_id=1321044729160859650&scene=189#rd)

#### MongoDB
库:
- Pymongo
    - from pymongo import MongoClient

### 数据可视化
[Link](https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484538&idx=1&sn=d9b614201c96ad283bbad8a867d42082&chksm=fc8bbcebcbfc35fd6012625979a88c2bf8c5bbf81dbd265b2ab9326972d4266e621d5b190d23&cur_album_id=1321044729160859650&scene=189#rd)
好用的库：
- matplotlib
    - python -m pip install -U pip setuptools
    - python -m pip install matplotlib
    - [matplotlib](https://matplotlib.org/2.0.2/contents.html)
- seaborn
    - [seaborn](https://seaborn.pydata.org/index.html)
- pyecharts
    - 百度开源可视化库
    - 很酷炫
    - [Link](https://pyecharts.org)

### Scrapy
```
scrapy startproject projectname
scrapy crawl projectname
```

### Chrome extentions
- ChroPath
    - 一键获取xpath、css selector
- Web Scraper
     - 直接爬取数据
     - [Link](https://webscraper.io/)

### 字体css加密
- [Link](https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484921&idx=1&sn=72a707c5bc67eede144947829cab4dc6&chksm=fc8bbd68cbfc347eca6727ff90f85ef58a4fdd7c2f75a962aee3ccd5e9c4266dbe5f4e6e2262&cur_album_id=1321044729160859650&scene=189#rd)

### js加密
-[Link](https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484997&idx=1&sn=b304304aacb3cba31f5f7a6c6bb1ba69&chksm=fc8bbed4cbfc37c29db631c187295757c164ae75ff3e0381dbbf685a9f3d1410098e5b751e33&cur_album_id=1321044729160859650&scene=189#rd)

### 爬虫小技巧
1. 移动端页面可能反爬会少一些
2. 克制一些:sleep 以及 半夜爬
3. 选用robots.txt里的UA
4. 找到sitemap获取url

### python运行js的库
- js2py
- PyV8
- PyExecJS




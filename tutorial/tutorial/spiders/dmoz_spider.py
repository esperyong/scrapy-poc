# coding: utf-8
from scrapy.spider import BaseSpider

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
        "http://news.sina.com.cn/china/",
        "http://zhusuban.xdf.cn/?utm_campaign=jituan_sohu_shouye_wenzilian_zhusuban_717z731&utm_medium=sohu&utm_source=cpm&utm_content=&utm_term=",
    ]

    def parse(self, response):
        print "爬爬<%s>" % response.url
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)



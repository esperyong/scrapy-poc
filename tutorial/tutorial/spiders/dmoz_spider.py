# coding: utf-8
from scrapy.spider import BaseSpider
from scrapy.utils.misc import arg_to_iter
from scrapy.http.request import Request
from scrapy.selector import HtmlXPathSelector
class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["sina.com.cn"]

    def __init__(self, name=None, **kwargs):
        if name is not None:
            self.name = name
        elif not getattr(self, 'name', None):
            raise ValueError("%s must have a name" % type(self).__name__)
        self.__dict__.update(kwargs)
        if not hasattr(self, 'start_urls'):
            self.start_urls = [
                "http://news.sina.com.cn",
                "http://www.sina.com.cn",
            ]

    def parse(self, response):
        print "爬爬<%s>" % response.url
        print response.headers
        hxs = HtmlXPathSelector(response)
        print hxs.select('//title').extract()
        if response.headers.has_key('Last-Modified'):
            response_headers = {'If-Modified-Since':
                                response.headers['Last-Modified']}
        req = Request(response.url, dont_filter=True,headers=response_headers)
        reqs = [req]
        return reqs



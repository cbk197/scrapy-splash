# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 10:59:12 2019

@author: ironman
"""

import scrapy
from scrapy_splash import SplashRequest


script = """ 
function main(splash)
    splash:init_cookies(splash.args.cookies)
    local url = splash.args.url
    assert(splash:go(url))
    assert(splash:wait(5))
    return {
        cookies = splash:get_cookies(),
        html = splash:html()
    }
end
"""

script2 = """
function main(splash)
    splash:init_cookies(splash.args.cookies)
    local url = splash.args.url
    assert(splash:go(url))
    assert(splash:wait(0.5))
    return {
        cookies = splash:get_cookies(),
        html = splash:html()
    }
end
"""

script3 = """
function main(splash)
    splash:wait(5)
    local scroll_screen = splash:jsfunc([[
        function () {
            window.scrollTo(0,document.body.scrollHeight);
            return document.body.scrollHeight
        }
    ]])
    local last_scroll_height = 0
    local scroll_height = scroll_screen()
    while last_scroll_height < scroll_height do
        last_scroll_height = scroll_height
        scroll_height = scroll_screen()
        splash:wait(3)
    end
end
"""

class FahasaSpider(scrapy.Spider):
    name = 'fahasa'
    allowed_domains = ['youtube.com']
    start_urls = [
        
      "https://www.youtube.com/watch?v=sFUHKzXWrR4"
        ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse )

    def parse(self, response):
        # Get the next page and yield Request
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,endpoint='execute',
                                args={'lua_source': script3} )
        page = response.url.split("/")[-3]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        # Get URL in page and yield Request
       
    def parse_item(self, response):
        """
        Handle crawl logic here
        """
        pass
        
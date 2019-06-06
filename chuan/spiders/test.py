# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 10:59:12 2019

@author: ironman
"""

import scrapy
from scrapy_splash import SplashRequest
from scrapy.selector import Selector
import datetime
import time
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.http import FormRequest
from scrapy.spiders import CrawlSpider
from chuan.items import InforItem, CommentField, ReplyField

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
function main(splash, args)
    local num_scrolls = args.nums
    local tmp = 0
  	splash.private_mode_enabled = false
    local get_body_height = splash:jsfunc(
        "function() {return document.body.scrollHeight;}"
    )
    assert(splash:go(splash.args.url))
    assert(splash:wait(20))
    splash:set_viewport_full()
    local body_heigh = get_body_height()
  	local count = 0 
  	local elemet1 
  	local showmore
  	while count < num_scrolls do
        count = count + 1
        tmp = tmp + 300
        if tmp < body_heigh - 300 then
            splash.scroll_position= {0,tmp}
            assert(splash:wait(0.1))
        else
            splash.scroll_position= {0,tmp}
      		assert(splash:wait(6))
      		
        end
    	element1 = splash:select_all('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer paper-button#more.style-scope.ytd-expander div.more-button.style-scope.ytd-comment-replies-renderer')
    	for _,elm in ipairs(element1) do
            elm:click()
            assert(splash:wait(1))
        end
        element2 = splash:select_all('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer div#content.style-scope.ytd-expander div#continuation.style-scope.ytd-comment-replies-renderer yt-next-continuation.style-scope.ytd-comment-replies-renderer paper-button.style-scope.yt-next-continuation yt-formatted-string.style-scope.yt-next-continuation')
        local element3 = splash:select('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer div#content.style-scope.ytd-expander div#continuation.style-scope.ytd-comment-replies-renderer yt-next-continuation.style-scope.ytd-comment-replies-renderer paper-button.style-scope.yt-next-continuation yt-formatted-string.style-scope.yt-next-continuation')
    	while element3 ~= nil do
            for _,elm in ipairs(element2) do
                elm:click()
                assert(splash:wait(1))
            end
            element2 = splash:select_all('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer div#content.style-scope.ytd-expander div#continuation.style-scope.ytd-comment-replies-renderer yt-next-continuation.style-scope.ytd-comment-replies-renderer paper-button.style-scope.yt-next-continuation yt-formatted-string.style-scope.yt-next-continuation')
        end
        body_heigh = get_body_height();
    end
  	
    return splash:html()
  
end

"""

script3 = """
function main(splash)
    local num_scrolls = 2
    local tmp = 0
  	splash.private_mode_enabled = false
    local get_body_height = splash:jsfunc(
        "function() {return document.body.scrollHeight;}"
    )
    assert(splash:go(splash.args.url))
    assert(splash:wait(20))
    splash:set_viewport_full()
  	splash.scroll_position= {0,300}
    assert(splash:wait(15))
    local body_heigh = get_body_height()
  	local count = 0 
  	local elemet1 
  	local showmore
  	while tmp < body_heigh do
        tmp = body_heigh
        local body = splash:select('html body')
      	body:send_keys('PageDown')
      	assert(splash:wait(10))
      	
        
    	element1 = splash:select_all('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer paper-button#more.style-scope.ytd-expander div.more-button.style-scope.ytd-comment-replies-renderer')
    	for _,elm in ipairs(element1) do
            elm:click()
            assert(splash:wait(8))
        end
        element2 = splash:select_all('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer div#content.style-scope.ytd-expander div#continuation.style-scope.ytd-comment-replies-renderer yt-next-continuation.style-scope.ytd-comment-replies-renderer paper-button.style-scope.yt-next-continuation yt-formatted-string.style-scope.yt-next-continuation')
        local element3 = splash:select('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer div#content.style-scope.ytd-expander div#continuation.style-scope.ytd-comment-replies-renderer yt-next-continuation.style-scope.ytd-comment-replies-renderer paper-button.style-scope.yt-next-continuation yt-formatted-string.style-scope.yt-next-continuation')
    	while element3 ~= nil do
            for _,elm in ipairs(element2) do
                elm:click()
                assert(splash:wait(8))
            end
            element2 = splash:select_all('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer div#content.style-scope.ytd-expander div#continuation.style-scope.ytd-comment-replies-renderer yt-next-continuation.style-scope.ytd-comment-replies-renderer paper-button.style-scope.yt-next-continuation yt-formatted-string.style-scope.yt-next-continuation')
			element3 = splash:select('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer div#content.style-scope.ytd-expander div#continuation.style-scope.ytd-comment-replies-renderer yt-next-continuation.style-scope.ytd-comment-replies-renderer paper-button.style-scope.yt-next-continuation yt-formatted-string.style-scope.yt-next-continuation')       
    	end
        body_heigh = get_body_height();	
    end
  	
    return splash:html()
  
end

"""





class FahasaSpider(scrapy.Spider):
    name = 'you1'
    
    allowed_domains = ['youtube.com','google.com','accounts.google.com']
    start_urls = [
        
      "https://www.youtube.com/watch?v=4_Ba3ENek2Q&t=1186s"
    ]


    

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, endpoint='execute',
                                args={'wait': 10,'lua_source': script3, 'timeout':3600, 'nums': 10}, callback = self.parse )

    def parse(self, response):
        # Get the next page and yield Request
        # for url in self.start_urls:
        #     yield SplashRequest(url, self.parse,endpoint='execute',
        #                         args={'lua_source': script3} )
        item = InforItem()
        
        
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        print("\n\n\n\n\n response url %s" %response.url)
        # comment= response.selector.xpath('//*[@id="content-text"]')
        # replie = response.selector.css('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer div#content.style-scope.ytd-expander div#expander-contents.style-scope.ytd-comment-replies-renderer div#loaded-replies.style-scope.ytd-comment-replies-renderer ytd-comment-renderer.style-scope.ytd-comment-replies-renderer div#body.style-scope.ytd-comment-renderer div#main.style-scope.ytd-comment-renderer ytd-expander#expander.style-scope.ytd-comment-renderer div#content.style-scope.ytd-expander yt-formatted-string#content-text.style-scope.ytd-comment-renderer')
        comment = response.selector.css('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer')
                                         
        i = 0
        listcomment = []
        for xtext in comment: 
            listreply = []
            itemcomment = CommentField()                      
            commentPart= xtext.css('ytd-comment-renderer#comment.style-scope.ytd-comment-thread-renderer div#body.style-scope.ytd-comment-renderer div#main.style-scope.ytd-comment-renderer')
            commenttex= commentPart.css('ytd-expander#expander.style-scope.ytd-comment-renderer div#content.style-scope.ytd-expander yt-formatted-string#content-text.style-scope.ytd-comment-renderer')
            like = commentPart.css('ytd-comment-action-buttons-renderer#action-buttons.style-scope.ytd-comment-renderer div#toolbar.style-scope.ytd-comment-action-buttons-renderer span#vote-count-middle.style-scope.ytd-comment-action-buttons-renderer')
            itemcomment["Content"] = commenttex.select("text()").extract_first()
            itemcomment["Like"] = like.select("text()").extract_first()
            itemcomment["DisLike"] = 0
            
            j = 0
            replie = xtext.css('div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer div#content.style-scope.ytd-expander div#expander-contents.style-scope.ytd-comment-replies-renderer div#loaded-replies.style-scope.ytd-comment-replies-renderer ytd-comment-renderer.style-scope.ytd-comment-replies-renderer div#body.style-scope.ytd-comment-renderer div#main.style-scope.ytd-comment-renderer ytd-expander#expander.style-scope.ytd-comment-renderer div#content.style-scope.ytd-expander yt-formatted-string#content-text.style-scope.ytd-comment-renderer')
            # if replie != [] :
            #     print("\n\nreplies========================================================:\n\n\n")
                
            for text in replie: 
                itemReplies = ReplyField()
                itemReplies["Content"] = text.select("text()").extract_first()
                
                j= j+1
                listreply.append(dict(itemReplies))
            itemcomment["Replies"] = list(listreply)
            itemcomment["CountReplies"] = j+1
            listcomment.append(dict(itemcomment))
            i = i+1
        item["CountComment"] = i
        item["Comment"] = list(listcomment)
        print("\n\n\n\n number comment: ",i)
        
        
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' %filename)
        
        # Get URL in page and yield Request 

    
    def parse_item(self, response):
        """
        Handle crawl logic here
        """
        pass
        
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 10:59:12 2019

@author: ironman
"""

import scrapy
from scrapy_splash import SplashRequest
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import datetime
import time
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.http import FormRequest
from scrapy.spiders import CrawlSpider
from chuan.items import InforItem, CommentField, ReplyField
from bs4 import BeautifulSoup
import os
import os.path
import random


scriptNumComment = """
function main(splash,args)
    local num_scrolls = args.nums
    local tmp = 0
  	splash.private_mode_enabled = false
    splash.request_body_enabled = true
    splash.html5_media_enabled = true
    splash.images_enabled = false
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
  	while tmp < num_scrolls do
        tmp = tmp+1
        splash.scroll_position= {0,body_heigh}
      	assert(splash:wait(8))
      	
        
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
			element3 = splash:select('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer div#content.style-scope.ytd-expander div#continuation.style-scope.ytd-comment-replies-renderer yt-next-continuation.style-scope.ytd-comment-replies-renderer paper-button.style-scope.yt-next-continuation yt-formatted-string.style-scope.yt-next-continuation')       
    	end
        assert(splash:wait(5))
        body_heigh = get_body_height();	
        
    end
  	
    return splash:html()
  
end

"""

scriptFullComment = """
function main(splash)
    local num_scrolls = 2
    local tmp = 0
  	splash.private_mode_enabled = false
    splash.request_body_enabled = true
    splash.html5_media_enabled = true
    splash.images_enabled = false
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
      	
        splash.scroll_position= {0,body_heigh}
      	assert(splash:wait(8))
      	
        
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
			element3 = splash:select('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer div#content.style-scope.ytd-expander div#continuation.style-scope.ytd-comment-replies-renderer yt-next-continuation.style-scope.ytd-comment-replies-renderer paper-button.style-scope.yt-next-continuation yt-formatted-string.style-scope.yt-next-continuation')       
    	end
        assert(splash:wait(5))
        body_heigh = get_body_height();	
        
    end
  	
    return splash:html()
  
end

"""

scriptCommentFullNoReply = """
function main(splash)
    
    local tmp = 0
  	splash.private_mode_enabled = false
    splash.request_body_enabled = true
    splash.html5_media_enabled = true
    splash.images_enabled = false
    local get_body_height = splash:jsfunc(
        "function() {return document.body.scrollHeight;}"
    )
    assert(splash:go(splash.args.url))
    assert(splash:wait(20))
    splash:set_viewport_full()
  	splash.scroll_position= {0,300}
    assert(splash:wait(15))
    local body_heigh = get_body_height()
  	
  	while tmp < body_heigh do
        tmp = body_heigh
        local body = splash:select('html body')
      	
        splash.scroll_position= {0,body_heigh}
      	assert(splash:wait(8))
      	
        body_heigh = get_body_height();	
        
    end
  	
    return splash:html()
  
end
"""

scriptNumCommentNoReply = """ 
function main(splash,args)
    local num_scrolls = args.nums
    local tmp = 0
  	splash.private_mode_enabled = false
    splash.request_body_enabled = true
    splash.html5_media_enabled = true
    splash.images_enabled = false
    local get_body_height = splash:jsfunc(
        "function() {return document.body.scrollHeight;}"
    )
    assert(splash:go(splash.args.url))
    assert(splash:wait(20))
    splash:set_viewport_full()
    local body_heigh = get_body_height()
  	while tmp < num_scrolls do
        tmp = tmp+1
        splash.scroll_position= {0,body_heigh}
      	assert(splash:wait(8))
      	
        body_heigh = get_body_height();	
        
    end
  	
    return splash:html()
  
end
"""
chanelScriptGetAll = """
function main(splash,args)
    local num_scrolls = args.nums
    local tmp = 0
  	splash.private_mode_enabled = false
    splash.images_enabled = false
    local get_body_height = splash:jsfunc(
        "function() {return document.body.scrollHeight;}"
    )
    assert(splash:autoload("https://code.jquery.com/jquery-2.1.3.min.js"))
    assert(splash:go(splash.args.url))
    assert(splash:wait(15))
    splash:set_viewport_full()
    local body_heigh = get_body_height();	
    while tmp < num_scrolls do
        tmp = tmp+1
        splash.scroll_position= {0,body_heigh}
      	assert(splash:wait(15))
        body_heigh = get_body_height();	
    end
    
    return splash:html()
    
end
"""


dataJson = None
ChanelDirctory = None
PathDir= None
class CrawlVideo(scrapy.Spider):
    
    name = 'youtube'
    
    allowed_domains = ['youtube.com','google.com','accounts.google.com']
    start_urls = []
    
   

    def start_requests(self):
        f = open("chuan\infor.json",'r')
        data = f.read()
        global dataJson
        global PathDir
        dataJson = json.loads(data)
        if dataJson['ChanelUrl'] == None :
            self.start_urls.append(dataJson['VideoUrl'])
            PathDir = "chuan\data\\video"
            if  not os.path.exists(PathDir) :
                os.mkdir(PathDir)
            for url in self.start_urls:
                if dataJson['MaxComment'] == -1:
                    if dataJson['Replies'] ==-1:
                        yield SplashRequest(url, endpoint='execute',
                                            args={'wait': 20,'lua_source': scriptFullComment, 'timeout':3600}, callback = self.parse )
                    else :
                        yield SplashRequest(url, endpoint='execute',
                                            args={'wait': 20,'lua_source': scriptCommentFullNoReply, 'timeout':3600}, callback = self.parse )
                
                else:
                    num = int(dataJson['MaxComment']/20 + 1) 
                    if dataJson['Replies'] == -1 :

                        yield SplashRequest(url, endpoint='execute',
                                            args={'wait': 20,'lua_source': scriptNumComment, 'timeout':3600,'nums': num}, callback = self.parse )
                    else:
                        yield SplashRequest(url, endpoint='execute',
                                            args={'wait': 20,'lua_source': scriptNumCommentNoReply, 'timeout':3600,'nums': num}, callback = self.parse )

        else : 
            chanelUrl = dataJson['ChanelUrl']
            index = chanelUrl.find('www.youtube.com')
            outUrl = chanelUrl[:index]+'m'+ chanelUrl[index+3:]
            self.start_urls.append(dataJson['ChanelUrl']+'/videos')
            num = int(dataJson['MaxVideo']/30 + 1)
            
            for url in self.start_urls:
                yield SplashRequest(url, endpoint='execute',
                                    args={'wait': 20,'lua_source': chanelScriptGetAll, 'timeout':3600, 'nums': num}, callback = self.parseChanel )



    def parse(self, response):
        # Get the next page and yield Request
        # for url in self.start_urls:
        #     yield SplashRequest(url, self.parse,endpoint='execute',
        #                         args={'lua_source': script3} )

        
        item = InforItem()
        global dataJson
        # comment= response.selector.xpath('//*[@id="content-text"]')
        # replie = response.selector.css('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer div#content.style-scope.ytd-expander div#expander-contents.style-scope.ytd-comment-replies-renderer div#loaded-replies.style-scope.ytd-comment-replies-renderer ytd-comment-renderer.style-scope.ytd-comment-replies-renderer div#body.style-scope.ytd-comment-renderer div#main.style-scope.ytd-comment-renderer ytd-expander#expander.style-scope.ytd-comment-renderer div#content.style-scope.ytd-expander yt-formatted-string#content-text.style-scope.ytd-comment-renderer')
        comment = response.selector.css('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#contents.style-scope.ytd-item-section-renderer ytd-comment-thread-renderer.style-scope.ytd-item-section-renderer')
        item['Title'] = response.css('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy div#info.style-scope.ytd-watch-flexy div#info-contents.style-scope.ytd-watch-flexy ytd-video-primary-info-renderer.style-scope.ytd-watch-flexy div#container.style-scope.ytd-video-primary-info-renderer h1.title.style-scope.ytd-video-primary-info-renderer yt-formatted-string.style-scope.ytd-video-primary-info-renderer').select("text()").extract_first().strip()
        item['View'] = response.css('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy div#info.style-scope.ytd-watch-flexy div#info-contents.style-scope.ytd-watch-flexy ytd-video-primary-info-renderer.style-scope.ytd-watch-flexy div#container.style-scope.ytd-video-primary-info-renderer div#info.style-scope.ytd-video-primary-info-renderer div#info-text.style-scope.ytd-video-primary-info-renderer div#count.style-scope.ytd-video-primary-info-renderer yt-view-count-renderer.style-scope.ytd-video-primary-info-renderer span.view-count.style-scope.yt-view-count-renderer').select("text()").extract_first().strip()
        item['Like'] = response.css('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy div#info.style-scope.ytd-watch-flexy div#info-contents.style-scope.ytd-watch-flexy ytd-video-primary-info-renderer.style-scope.ytd-watch-flexy div#container.style-scope.ytd-video-primary-info-renderer div#info.style-scope.ytd-video-primary-info-renderer div#menu-container.style-scope.ytd-video-primary-info-renderer div#menu.style-scope.ytd-video-primary-info-renderer ytd-menu-renderer.style-scope.ytd-video-primary-info-renderer div#top-level-buttons.style-scope.ytd-menu-renderer ytd-toggle-button-renderer.style-scope.ytd-menu-renderer.force-icon-button.style-default-active a.yt-simple-endpoint.style-scope.ytd-toggle-button-renderer yt-formatted-string#text.style-scope.ytd-toggle-button-renderer.style-default-active').select("text()").extract_first()
        item['DisLike'] = response.css('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy div#info.style-scope.ytd-watch-flexy div#info-contents.style-scope.ytd-watch-flexy ytd-video-primary-info-renderer.style-scope.ytd-watch-flexy div#container.style-scope.ytd-video-primary-info-renderer div#info.style-scope.ytd-video-primary-info-renderer div#menu-container.style-scope.ytd-video-primary-info-renderer div#menu.style-scope.ytd-video-primary-info-renderer ytd-menu-renderer.style-scope.ytd-video-primary-info-renderer div#top-level-buttons.style-scope.ytd-menu-renderer ytd-toggle-button-renderer.style-scope.ytd-menu-renderer.force-icon-button.style-text a.yt-simple-endpoint.style-scope.ytd-toggle-button-renderer yt-formatted-string#text.style-scope.ytd-toggle-button-renderer.style-text').select("text()").extract_first()
        item['CountComment'] = response.css('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy ytd-comments#comments.style-scope.ytd-watch-flexy ytd-item-section-renderer#sections.style-scope.ytd-comments div#header.style-scope.ytd-item-section-renderer ytd-comments-header-renderer.style-scope.ytd-item-section-renderer div#title.style-scope.ytd-comments-header-renderer h2#count.style-scope.ytd-comments-header-renderer yt-formatted-string.count-text.style-scope.ytd-comments-header-renderer').select("text()").extract_first()
        item['ChanelName'] = response.css('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy div#meta.style-scope.ytd-watch-flexy div#meta-contents.style-scope.ytd-watch-flexy ytd-video-secondary-info-renderer.style-scope.ytd-watch-flexy div#container.style-scope.ytd-video-secondary-info-renderer div#top-row.style-scope.ytd-video-secondary-info-renderer ytd-video-owner-renderer.style-scope.ytd-video-secondary-info-renderer div#upload-info.style-scope.ytd-video-owner-renderer div#owner-container.style-scope.ytd-video-owner-renderer yt-formatted-string#owner-name.style-scope.ytd-video-owner-renderer a.yt-simple-endpoint.style-scope.yt-formatted-string').select("text()").extract_first().strip()
        item['ChanelLink'] = response.css('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy div#meta.style-scope.ytd-watch-flexy div#meta-contents.style-scope.ytd-watch-flexy ytd-video-secondary-info-renderer.style-scope.ytd-watch-flexy div#container.style-scope.ytd-video-secondary-info-renderer div#top-row.style-scope.ytd-video-secondary-info-renderer ytd-video-owner-renderer.style-scope.ytd-video-secondary-info-renderer div#upload-info.style-scope.ytd-video-owner-renderer div#owner-container.style-scope.ytd-video-owner-renderer yt-formatted-string#owner-name.style-scope.ytd-video-owner-renderer a.yt-simple-endpoint.style-scope.yt-formatted-string').xpath("@href").extract_first().strip()
        item['ChanelSub'] = response.css('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton div#columns.style-scope.ytd-watch-flexy div#primary.style-scope.ytd-watch-flexy div#primary-inner.style-scope.ytd-watch-flexy div#meta.style-scope.ytd-watch-flexy div#meta-contents.style-scope.ytd-watch-flexy ytd-video-secondary-info-renderer.style-scope.ytd-watch-flexy div#container.style-scope.ytd-video-secondary-info-renderer div#top-row.style-scope.ytd-video-secondary-info-renderer div#subscribe-button.style-scope.ytd-video-secondary-info-renderer ytd-subscribe-button-renderer.style-scope.ytd-video-secondary-info-renderer paper-button.style-scope.ytd-subscribe-button-renderer yt-formatted-string.style-scope.ytd-subscribe-button-renderer span.deemphasize.style-scope.yt-formatted-string').select("text()").extract_first()
        item['Url'] = response.url
        i = 0
        listcomment = []
        if dataJson['MaxComment']  != 0 :
            
            for xtext in comment: 
                if i == dataJson['MaxComment'] :
                    break
                if xtext != None:
                    listreply = []
                    itemcomment = CommentField()                      
                    commentPart= xtext.css('ytd-comment-renderer#comment.style-scope.ytd-comment-thread-renderer div#body.style-scope.ytd-comment-renderer div#main.style-scope.ytd-comment-renderer')
                    commenttex= commentPart.css('ytd-expander#expander.style-scope.ytd-comment-renderer div#content.style-scope.ytd-expander yt-formatted-string#content-text.style-scope.ytd-comment-renderer')
                    likeComment = commentPart.css('ytd-comment-action-buttons-renderer#action-buttons.style-scope.ytd-comment-renderer div#toolbar.style-scope.ytd-comment-action-buttons-renderer span#vote-count-middle.style-scope.ytd-comment-action-buttons-renderer')
                    NameComment = xtext.css('ytd-comment-renderer#comment.style-scope.ytd-comment-thread-renderer div#body.style-scope.ytd-comment-renderer div#main.style-scope.ytd-comment-renderer div#header.style-scope.ytd-comment-renderer div#header-author.style-scope.ytd-comment-renderer a#author-text.yt-simple-endpoint.style-scope.ytd-comment-renderer')

                    itemcomment['Name'] = NameComment.css('span.style-scope.ytd-comment-renderer').select("text()").extract_first().strip()
                    itemcomment['LinkName'] = NameComment.xpath("@href").extract_first().strip()
                    itemcomment["Content"] = commenttex.select("text()").extract_first()

                    if dataJson['LikeComment'] == -1 : 
                        itemcomment["Like"] = likeComment.select("text()").extract_first().strip()

                    if dataJson['DisLikeComment'] == -1 :
                        itemcomment["DisLike"] = 0

                    j = 0
                    if dataJson['Replies'] == -1 :

                        replie = xtext.css('div#replies.style-scope.ytd-comment-thread-renderer ytd-comment-replies-renderer.style-scope.ytd-comment-thread-renderer ytd-expander#expander.style-scope.ytd-comment-replies-renderer div#content.style-scope.ytd-expander div#expander-contents.style-scope.ytd-comment-replies-renderer div#loaded-replies.style-scope.ytd-comment-replies-renderer ytd-comment-renderer.style-scope.ytd-comment-replies-renderer div#body.style-scope.ytd-comment-renderer div#main.style-scope.ytd-comment-renderer')
                        if replie != None :
                            for text in replie: 
                                itemReplies = ReplyField()
                                replyContent = text.css('ytd-expander#expander.style-scope.ytd-comment-renderer div#content.style-scope.ytd-expander yt-formatted-string#content-text.style-scope.ytd-comment-renderer')
                                itemReplies["Content"] = replyContent.select("text()").extract_first()
                                if dataJson['LikeReplies'] == -1 :
                                    itemReplies['Like'] = text.css('ytd-comment-action-buttons-renderer#action-buttons.style-scope.ytd-comment-renderer div#toolbar.style-scope.ytd-comment-action-buttons-renderer span#vote-count-middle.style-scope.ytd-comment-action-buttons-renderer').select("text()").extract_first().strip()
                                if dataJson['DisLikeReplies'] == -1 :
                                    itemReplies['DisLike'] = 0 
                                itemReplies['Name'] = text.css('div#header.style-scope.ytd-comment-renderer div#header-author.style-scope.ytd-comment-renderer a#author-text.yt-simple-endpoint.style-scope.ytd-comment-renderer span.style-scope.ytd-comment-renderer').select("text()").extract_first().strip()
                                itemReplies['LinkName'] = text.css('div#header.style-scope.ytd-comment-renderer div#header-author.style-scope.ytd-comment-renderer a#author-text.yt-simple-endpoint.style-scope.ytd-comment-renderer').xpath("@href").extract_first().strip()
                                j= j+1
                                listreply.append(dict(itemReplies))
                                # print("\n\nreplies: ",dict(itemReplies))
                    itemcomment["Replies"] = list(listreply)
                    itemcomment["CountReplies"] = j
                    listcomment.append(dict(itemcomment))
                    i = i+1

        item["CountComment"] = i
        item["Comment"] = list(listcomment)
        global PathDir
        filename1 =  item['Title'] + str(random.randint(0,10000)) +  '.json'
        filename2 = filename1.replace(' ', '_')
        filename3 = filename2.replace('|', '_')
        filename4 = filename3.replace('*', '_')
        filename5 = filename4.replace('\\', '_')
        filename5 = filename5.replace('?', '_')
        filename5 = filename5.replace(':', '_')
        filename5 = filename5.replace('\"', '_')
        filename = PathDir + '\\' + filename5.replace('/', '_')
        
        f = open(filename,'w',encoding='utf-8')
        
        json.dump(dict(item),f,ensure_ascii= False)
        
        f.close()
            
        
        
        
        
        # Get URL in page and yield Request 

    
    def parseChanel(self,response):
        # soup = BeautifulSoup(response.body,'html.parser')
        # sel = Selector(text=soup.prettify())
        
        requestUrl = []
        linkVideo = response.selector.xpath('//div[@id="meta"]')
        
        i = 0
        global ChanelDirctory
        
        for link in linkVideo:
            # print("linkkkkk:",link.css('h3.style-scope.ytd-grid-video-renderer a#video-title.yt-simple-endpoint.style-scope.ytd-grid-video-renderer').xpath("@href").extract_first())
            if link.css('h3.style-scope.ytd-grid-video-renderer a#video-title.yt-simple-endpoint.style-scope.ytd-grid-video-renderer').xpath("@href").extract_first() != None:
                i = i+1
                requestUrl.append('https://www.youtube.com'+link.css('h3.style-scope.ytd-grid-video-renderer a#video-title.yt-simple-endpoint.style-scope.ytd-grid-video-renderer').xpath("@href").extract_first())
        
        
        numVideo = 0 
        ChanelDirctory = response.css('html body ytd-app div#content.style-scope.ytd-app ytd-page-manager#page-manager.style-scope.ytd-app ytd-browse.style-scope.ytd-page-manager div#header.style-scope.ytd-browse ytd-c4-tabbed-header-renderer.style-scope.ytd-browse app-header-layout.style-scope.ytd-c4-tabbed-header-renderer div#wrapper.style-scope.app-header-layout app-header#header.style-scope.ytd-c4-tabbed-header-renderer div#contentContainer.style-scope.app-header div#channel-container.style-scope.ytd-c4-tabbed-header-renderer div#channel-header.style-scope.ytd-c4-tabbed-header-renderer div#channel-header-container.style-scope.ytd-c4-tabbed-header-renderer div#inner-header-container.style-scope.ytd-c4-tabbed-header-renderer div#meta.style-scope.ytd-c4-tabbed-header-renderer h1#channel-title-container.style-scope.ytd-c4-tabbed-header-renderer span#channel-title.style-scope.ytd-c4-tabbed-header-renderer').select("text()").extract_first()
        global PathDir 
        
        filename1 =  ChanelDirctory + str(random.randint(0,10000)) 
        filename2 = filename1.replace(' ', '_')
        filename3 = filename2.replace('|', '_')
        filename4 = filename3.replace('*', '_')
        filename5 = filename4.replace('\\', '_')
        filename5 = filename5.replace('?', '_')
        filename5 = filename5.replace(':', '_')
        filename5 = filename5.replace('\"', '_')
        PathDir =  "chuan\data\chanel\\"+ filename5.replace('/', '_')
        try :
            os.mkdir(PathDir)
        except FileExistsError:
            print("create directory error. file name is exist")
        for url in requestUrl:
            if numVideo == dataJson['MaxVideo'] : 
                break
            numVideo = numVideo+ 1
            if dataJson['MaxComment'] == -1:
                if dataJson['Replies'] ==-1:
                    yield SplashRequest(url, endpoint='execute',
                                        args={'wait': 20,'lua_source': scriptFullComment, 'timeout':3600}, callback = self.parse )
                else :
                    yield SplashRequest(url, endpoint='execute',
                                        args={'wait': 20,'lua_source': scriptCommentFullNoReply, 'timeout':3600}, callback = self.parse )
                
            else:
                num = int(dataJson['MaxComment']/20 + 1) 
                if dataJson['Replies'] == -1 :

                    yield SplashRequest(url, endpoint='execute',
                                        args={'wait': 20,'lua_source': scriptNumComment, 'timeout':3600,'nums': num}, callback = self.parse )
                else:
                    yield SplashRequest(url, endpoint='execute',
                                        args={'wait': 20,'lua_source': scriptNumCommentNoReply, 'timeout':3600,'nums': num}, callback = self.parse )



        
        
                  
    def parseVideoList(self,response):
        Link = response.css('html body div div table tbody tr td div a')
        for link in Link: 
            print("link: %s"%link)
    def parse_item(self, response):
        """
        Handle crawl logic here
        """
        pass
        
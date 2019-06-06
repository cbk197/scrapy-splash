# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class ReplyField(scrapy.Item):
    Content = scrapy.Field(default='NULL')
    Like = scrapy.Field(default=0)
    DisLike = scrapy.Field(default=0)
    Name = scrapy.Field(default = 'NULL')
    LinkName = scrapy.Field(default = 'NULL')

class CommentField(scrapy.Item):
    Content = scrapy.Field(default='NULL')
    Replies = scrapy.Field(default='NULL')
    Like = scrapy.Field(default=0)
    DisLike = scrapy.Field(default=0)
    CountReplies = scrapy.Field(default=0)
    Name = scrapy.Field(default = 'NULL')
    LinkName = scrapy.Field(default = 'NULL')

class InforItem(scrapy.Item):
    Title = scrapy.Field(default='NULL')
    Like = scrapy.Field(default=0)
    View = scrapy.Field(default=0)
    DisLike = scrapy.Field(default=0)
    CountComment = scrapy.Field(default=0)
    ChanelName = scrapy.Field(default='NULL')
    ChanelSub = scrapy.Field(default=0)
    ChanelLink = scrapy.Field(default= 'NULL')
    Comment = scrapy.Field(default='NULL')
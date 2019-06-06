requie: installed python 3.7.3, docker, scrapy, splash

config input in infor.json :
    "ChanelUrl" : url of chanel for crawl data 
    "VideoUrl" : url of video for crawl data. if ChanelUrl is setted VideoUrl not pass.
    "MaxVideo" : if ChanelUrl is not NULL. this is maximum video will crawl data from chanel.
    "MaxComment": if value = -1 get all comment. else get 'value' comment per video 
    "Replies": if value = -1 get reply else dont get reply
    "LikeComment": value = -1 if like of comment of video need crawl else dont get like comment 
    "DisLikeComment": if value = -1 get DisLikeComment else dont get
    "LikeReplies" : if value = -1 get LikeReplies else dont get
    "DisLikeRplies": if value = -1 get DisLikeRplies else dont get


if ChanelUrl is NULL then crawl from VideoUrl.

run docker and after run command: "docker run -p 8050:8050 scrapinghub/splash --max-timeout 3600 --disable-lua-sandbox"
config port , browser in setings.py ( browser in my project is Firefox/66.0)

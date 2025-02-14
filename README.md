# scrapy-splash  

A web scraping project using **Scrapy** and **Splash** to extract data from video channels and comments.  

## 📌 Requirements  

Ensure you have the following installed before running the project:  

- **Python** 3.7.3  
- **Docker**  
- **Scrapy**  
- **Splash**  

## ⚙️ Configuration  

Modify the `info.json` file to customize your scraping settings:  

```json
{
    "ChannelUrl": "URL of the channel to crawl data from.",
    "VideoUrl": "URL of the video to crawl data from. If `ChannelUrl` is set, `VideoUrl` is not required.",
    "MaxVideo": "If `ChannelUrl` is not NULL, this specifies the maximum number of videos to crawl.",
    "MaxComment": "If set to `-1`, retrieves all comments; otherwise, limits the number of comments per video.",
    "Replies": "If set to `-1`, includes replies; otherwise, excludes replies.",
    "LikeComment": "If set to `-1`, retrieves like counts for comments; otherwise, excludes them.",
    "DisLikeComment": "If set to `-1`, retrieves dislike counts for comments; otherwise, excludes them.",
    "LikeReplies": "If set to `-1`, retrieves like counts for replies; otherwise, excludes them.",
    "DisLikeReplies": "If set to `-1`, retrieves dislike counts for replies; otherwise, excludes them."
}
```

## note
if ChanelUrl is NULL then crawl from VideoUrl.

## run splash with docker
run docker and after run command: "docker run -p 8050:8050 scrapinghub/splash --max-timeout 3600 --disable-lua-sandbox"
config port , browser in setings.py ( browser in my project is Firefox/66.0)

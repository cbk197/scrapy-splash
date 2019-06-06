config input in infor.json :
    ChanelUrl : url of chanel for crawl data 
    VideoUrl : url of video for crawl data. if ChanelUrl is setted VideoUrl not pass.
    MaxVideo : if ChanelUrl is not NULL. this is maximum video will crawl data from chanel.
    MaxCommentVideo : if ChanelUrl is NULL. MaxCommentVideo is maximum of comment need crawl of video from VideoUrl
    MaxCommentChanel : if ChanelUrl is not NULL. MaxCommentChanel is maximum number of comment will crawl from a video of chanel 
    RepliesVideo : if ChanelUrl is NULL. this is maximum number of replies need crawl from a comment of video from VideoUrl. default value is 0. it mean that no replies crawled.
    RepliesChanel : if ChanelUrl is not NULL. this is maximum number of replies need crawl per comment of a video from chanel.
    "LikeCommentVideo": value = 1 if like of comment of video need crawl else value = 0
    "DisLikeCommentVideo": 1,
    "LikeCommentChanel" : 1,
    "DisLikeCommentChanel" : 1,
    "LikeRepliesVideo" : 1,
    "DisLikeRpliesVideo": 1,
    "LikeRepliesChanel": 1,
    "DisLikeRepliesChanel": 1,
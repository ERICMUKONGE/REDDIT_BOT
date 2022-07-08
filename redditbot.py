import praw
import time

reddit = praw.Reddit(
    user_agent="Get Comments by /u/name",   
    client_id="ozVl7f8tW4wz2m05HtQ_XA",                        
    client_secret="-mrfXmew8UD2LM6iaWBLGrXHx2e9kw",
)

#list of subreddits to be post
#subreddits = ['SelfPromotionYoutube','Youtubeviews','videos','SubscribeToMe','YouTubePromoter','SmallYouTubeArmy','YoutubeSelfPromotion','shamelessplg','YouTubeScribeBoost','YouTube_startups','Youtubestartups','industrialized','AdvertiseYourVideo','GetMoreViewsYT','SmallYoutubers','madeinpython','girlsgonewired','codeprojects','coding','programming']
subreddits = ['SelfPromotionYoutube','Youtubeviews']
#title post of my reddit post

title="Sending the blackparnther as discord messages with python"
link = "https://www.youtube.com/watch?v=Nzo1sMATJL8"

count = 0
for subreddit in subreddits:
    count+=1
    try:
        reddit.subreddit(subreddits).submit(title, url=link, send_replies=False)
        print("Successfully posted to",subreddit,"Posted to",count,"of",len(subreddits),"subreddits")
    except praw.exceptions.RedditAPIException as exception:

        for subexception in exception.items:
            if subexception.error_type == "RATELIMIT":
                wait = str(subexception).replace("RATELIMIT:'you are doing that too much. try again in'","")

                if 'minute' in wait:
                    wait = wait[:2]
                    wait = int(wait)
                    print(wait) 
                else:
                    wait = 1
                print("waiting for:",wait,"minutes")
                time.sleep(wait*60)
                reddit.subreddit(subreddit).submit(title,url=link,send_replies=False)
                print("Sucessfully, posted to",subreddit,"Posted to",count,"of",len(subreddits),"subreddits")        

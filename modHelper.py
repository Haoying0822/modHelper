import os
import praw

reddit = praw.Reddit(
    username = os.environ.get('REDDIT_USERNAME'),
    password = os.environ.get('REDDIT_PASSWORD'),
    client_id = os.environ.get('API_CLIENT'),
    client_secret = os.enviorn.get('API_SECRET'),
    user_agent = "modHelper"
)

# only used for test now
for comment in reddit.subreddit("").comments(limit = 1000):
    if "tele" in comment.body.lower():
        comment.reply("tele link: ")

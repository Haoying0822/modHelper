import praw

reddit = praw.Reddit('modHelper')
subreddit = reddit.subreddit("pythonforengineers")

#Access the post in a subreddit
for submission in subreddit.hot(limit = 2):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

#Access the comments in a subreddit
subreddit_comments = subreddit.comments(limit = 10)
for comment in subreddit_comments:
    print(comment.id)
    print(comment.body)

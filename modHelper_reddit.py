from time import sleep
from urllib.request import urlopen
import praw
import pdb
import re
import requests
import os

reddit = praw.Reddit('modHelper')
subreddit = reddit.subreddit("nus") #currently we are testing our bot in this subreddit, after completed we will move to r/nus

while True:
    
    if not os.path.isfile("archive.txt"):
        archive = []
    else:
        with open("archive.txt", "r") as f:
            archive = f.read()
            archive = archive.split("\n")
            archive = list(filter(None, archive))

    for sub in subreddit.new(limit = 50):
        if sub.id not in archive:
            for com in sub.comments:
                if re.search("u/modHelper", com.body, re.IGNORECASE):
                    if re.search("tele", com.body, re.IGNORECASE): #this part need to collaborate with TeleNUS side
                          com.reply(body = "You may find your module group on this website: https://telenus.nusmods.com/ ^(This action is performed by a bot)")

                    elif re.search("mate", com.body, re.IGNORECASE):
                        com.reply(body = "You may wish to find your ideal groupmate in our telegram bot via this link: http://t.me/ModHelper_Bot ^(This action is performed by a bot)")

                    elif re.search("buddy", com.body, re.IGNORECASE):
                        com.reply(body = "You may wish to find your ideal study buddy in our telegram bot via this link: http://t.me/ModHelper_Bot ^(This action is performed by a bot)")
                    
                    archive.append(sub.id)
                

    with open("archive.txt", "w") as f:
        for post_id in archive:
            f.write(post_id + "\n")

    sleep(3600)

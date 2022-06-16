from time import sleep
from urllib.request import urlopen
import praw
import pdb
import re
import requests
import os

reddit = praw.Reddit('modHelper')
subreddit = reddit.subreddit("pythonforengineers") #currently we are testing our bot in this subreddit, after completed we will move to r/nus

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
                        module_code = com.body.split()[-1]
                        html_content = requests.request("GET", "https://telenus.nusmods.com/", verify = False).text
                        matches = re.findall(module_code, html_content)
                        if len(matches) == 0:
                          noTele_replyMsg = "The telegram group for module {0} is not found. You may follow the instructions here to create a group yourself: https://telenus.nusmods.com/".format(module_code)
                          com.reply(body = noTele_replyMsg)
                        else:
                          com.reply(body = module_code)

                    elif re.search("mate", com.body, re.IGNORECASE):
                        com.reply(body = "You may wish to find your ideal groupmate in our telegram bot via this link: http://t.me/ModHelper_Bot ^(This action is performed by a bot)")

                    elif re.search("buddy", com.body, re.IGNORECASE):
                        com.reply(body = "You may wish to find your ideal study buddy in our telegram bot via this link: http://t.me/ModHelper_Bot ^(This action is performed by a bot)")
                    
                    archive.append(sub.id)
                

    with open("archive.txt", "w") as f:
        for post_id in archive:
            f.write(post_id + "\n")

    sleep(3600)

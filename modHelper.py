from time import sleep
import praw
import pdb
import re
import os

reddit = praw.Reddit('modHelper')
subreddit = reddit.subreddit("pythonforengineers")

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
                    if re.search("tele", com.body, re.IGNORECASE):
                        module_code = com.body.split()[-1]
                        #com.reply(body = module_code + "\n***\n" + "^(This action is performed by a bot)")
                        com.reply(body = "https://telenus.nusmods.com/ ^(This action is performed by a bot)")


                        
                    '''elif re.search("mate", com.body, re.IGNORECASE):
                        pass
                    '''


                    
                    archive.append(sub.id)
                

    with open("archive.txt", "w") as f:
        for post_id in archive:
            f.write(post_id + "\n")

    sleep(3600)

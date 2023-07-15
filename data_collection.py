import praw
from requests import Session
from os import getenv
from dotenv import load_dotenv
from datetime import datetime as dt

load_dotenv()
session = Session()

now = dt.now().strftime("%Y-%m-%d %H:%M:%S")

#Connect to reddit server
reddit = praw.Reddit(
    client_id=getenv('client_id'),
    client_secret=getenv('client_secret'),
    requestor_kwargs={"session": session},
    user_agent=getenv('user_agent'),
    username=getenv('username'),
    password=getenv('password')
)
#defining subreddit
subreddit = reddit.subreddit("wallstreetbets")

#Writing to file - Hot topics
with open('hot.txt', 'a') as f:
    f.write('\n')
    f.write("------------------------------------------------------------------------------")
    f.write(now)
    f.write("\n")
    for hot in subreddit.hot(limit=100):
        f.write( hot.title)
        f.write("\n")

#Writing to file - New topics 
with open('new.txt', 'a') as f:
    f.write("\n")
    f.write("------------------------------------------------------------------------------")
    f.write(now)
    f.write("\n")
    for new in subreddit.new(limit=100):
        f.write( new.title)
        f.write("\n")

#Clean the data: read the files
hot = []
new = []
hot_file = open('hot.txt')
for line in hot_file.readlines():
    hot.append(line)
new_file = open('new.txt')
for line in new_file.readlines():
    new.append(line)

#remove any duplicate from the file.
hot = list(dict.fromkeys(hot))
new = list(dict.fromkeys(new))
#create a new array which selects hot topics from the new section
hot_and_new = list(set(hot).intersection(new))
# write to file
han_file = open('hot_and_new.txt', 'a')
han_file.write("------------------------------------------------------------------------------")
han_file.write(now)
han_file.write("\n")
for posts in hot_and_new:
    han_file.write(posts)
han_file.close()

print("Data Collected")
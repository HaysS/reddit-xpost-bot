#!/usr/bin/env python3

import json
import praw

data = json.load(open("config.json"))

for x in data:
    print("%s: %s" % (x, data[x]))

# print(data['client_secret'])

# create better system for managing these credentials
source = 'reactnative'
destination = 'expojs'

reddit = praw.Reddit(
    client_id=data['client_id'],
    client_secret=data['client_secret'],
    username=data['username'],
    password=data['password'],
    user_agent='script:xpost from one sub to another')

i = 0

submissions = reddit.subreddit(destination).stream.submissions()

for submission in submissions:
    print(i)
    i =i+1

# for submission in reddit.subreddit(source).top(time_filter='week'):
#     if not submission.is_self:
#     	print("submission.title: %s" % (submission.url))
        # reddit.subreddit(destination).submit(submission.title, url=submission.url)
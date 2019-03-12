#!/usr/bin/env python3

import json
import praw

data = json.load(open("config.json"))

for x in data:
    print("%s: %s" % (x, data[x]))

# print(data['client_secret'])

# create better system for managing these credentials
source = 'cybersecurity'
destination = 'infocyte'

reddit = praw.Reddit(
    client_id=data['client_id'],
    client_secret=data['client_secret'],
    username=data['username'],
    password=data['password'],
    user_agent='script:repost from one sub to another:v0.1:written by doug89')

for submission in reddit.subreddit(source).stream.submissions():
    if not submission.is_self:
        reddit.subreddit(destination).submit(submission.title, url=submission.url)
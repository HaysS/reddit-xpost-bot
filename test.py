#!/usr/bin/env python3

import json
import praw
from pprint import pprint

data = json.load(open("config.json"))

for x in data:
    print("%s: %s" % (x, data[x]))

# source = 'murica'
# destination = 'muricaspeaks'

# reddit = praw.Reddit(
#     client_id='xIl6p7Dg9nJd4g',
#     client_secret='XMNpldoRffi4UbFVuzRAUkmiSmk',
#     username='SynthesizeMeSun',
#     password='',
#     user_agent='script:repost from one sub to another:v0.1:written by doug89')

# for submission in reddit.subreddit(source).stream.submissions():
#     if not submission.is_self:
#         reddit.subreddit(destination).submit(submission.title, url=submission.url)
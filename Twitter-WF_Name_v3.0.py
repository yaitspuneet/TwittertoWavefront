#!/usr/bin/python

import json
import time

# Import the File Location to a Path Variable
tweets_data_path = '/Users/puneeta/PycharmProjects/Twitter/Wavefront + Twitter Demo/Wavefront_Metrics/Twitter-Data1.json'
tweets_out_path = '/Users/puneeta/PycharmProjects/Twitter/Wavefront + Twitter Demo/Wavefront_Metrics/Output.txt'

# For Loop for opening the JSOn file and Reading it line by line
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
#        print(tweet)
# Printing the Parsed data points in WF Metric format
        if '#nsx' in tweet['text']:
            print("vforum.twitter.sentiment", int("01"), int(time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))), 'source=vforum', 'user=', tweet['user']['screen_name'])
        elif '#vrealize' in tweet['text']:
            print("vforum.twitter.sentiment", int("02"), int(time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))), 'source=vforum', 'user=', tweet['user']['screen_name'])
        else:
            print("vforum.twitter.sentiment", int("05"), int(time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))), 'source=vforum', 'user=', tweet['user']['screen_name'])
    except:
        continue
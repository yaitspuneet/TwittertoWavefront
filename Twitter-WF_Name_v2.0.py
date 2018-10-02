#!/usr/bin/python

import json

# Import the File Location to a Path Variable
tweets_data_path = '/Users/puneeta/PycharmProjects/Twitter/Wavefront + Twitter Demo/Twitter_data.json'
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
            print("vforum.twitter.sentiment", "#nsx", tweet['created_at'], 'source=vforum')
        elif '#vrealize' in tweet['text']:
            print("vforum.twitter.sentiment", "#vrealize", tweet['created_at'], 'source=vforum')
        else:
            print("vforum.twitter.name", tweet['user']['screen_name'], tweet['created_at'], 'source=vforum', 'location=', tweet['user']['location'])
    except:
        continue
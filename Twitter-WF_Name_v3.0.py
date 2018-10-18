#!/usr/bin/python

import json
import time

# Import the File Location to a Path Variable
tweets_data_path = '/Users/puneeta/PycharmProjects/Twitter/Wavefront + Twitter Demo/Wavefront_Metrics/Twitter-Data9.json'

# For Loop for opening the JSOn file and Reading it line by line
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
#        print(tweet)
# Printing the Parsed data points in WF Metric format
        if '#NSX' in tweet['text'] or '#nsx' in tweet['text'] or '#security' in tweet['text']:
            print("vforum.twitter.dummydata1", int("01"), int(time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))), 'source=vforum', 'user=', tweet['user']['screen_name'], 'location=', tweet['user']['location'])
        elif '#Cloud' in tweet['text'] or '#vrealize' in tweet['text'] or '#vRealize' in tweet['text']:
            print("vforum.twitter.dummydata1", int("02"), int(time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))), 'source=vforum', 'user=', tweet['user']['screen_name'], 'location=', tweet['user']['location'])
        elif '#IOT' in tweet['text']:
            print("vforum.twitter.dummydata1", int("03"), int(time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))), 'source=vforum', 'user=', tweet['user']['screen_name'], 'location=', tweet['user']['location'])
        elif '#Mobility' in tweet['text']:
            print("vforum.twitter.dummydata1", int("04"), int(time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))), 'source=vforum', 'user=', tweet['user']['screen_name'], 'location=', tweet['user']['location'])
        elif '#vSAN' in tweet['text'] or '#VSAN' in tweet['text'] or '#vsan' in tweet['text']:
            print("vforum.twitter.dummydata1", int("05"), int(time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))), 'source=vforum', 'user=', tweet['user']['screen_name'], 'location=', tweet['user']['location'])
        elif '#vforum' in tweet['text'] or '#vForum' in tweet['text'] or '#vForumIN' in tweet['text'] or '#vmware' in tweet['text'] or '#VMware' in tweet['text']:
            print("vforum.twitter.dummydata1", int("06"), int(time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))), 'source=vforum', 'user=', tweet['user']['screen_name'], 'location=', tweet['user']['location'])
    except:
        continue

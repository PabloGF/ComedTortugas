#!/usr/bin/env python
import tweepy
import re
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweets = api.search(q="comed, tortugas!")
tweets = [tweet for tweet in tweets if re.match("^comed,? tortugas!?$", tweet.text.lower())]

for tweet in tweets:
    sn = tweet.user.screen_name
    m = "[TEST] Gracias por darnos de comer, @%s! Si vienes a la @OSHWDem, te lo agradeceremos personalmente!" % (sn)
    s = api.update_status(m, tweet.id)


#!/usr/bin/env python
import tweepy
import re
import random
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

PATH_FICHEIRO="/home/ch01/.tweets_enviados"

def get_enviados (path):
	try:
		with open(path, "r") as archivo:
			return [int(line) for line in archivo.split("\n")]
	except:
		return []

def set_enviados (path, lista):
	with open(path, "w") as archivo:
		 archivo.write("\n".join([str(x) for x in lista]))



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

enviados = get_enviados (PATH_FICHEIRO)

tweets = api.search(q="comed, tortugas!")
tweets = [tweet for tweet in tweets if re.match("^comed,? tortugas!?$", tweet.text.lower())]
tweets = [tweet for tweet in tweets if tweet.id not in enviados]

random.shuffle(tweets)


for tweet in tweets:
    sn = tweet.user.screen_name
    m = "[TEST] Gracinhas por darnos de comer, @%s! Se ves a @OSHWDem, agradeceremocho persoalmente!" % (sn)
    try:
    	s = api.update_status(m, tweet.id)
    	enviados.append(tweet.id)
    	print "Tweet replied to @%s :)" % (sn)
    except tweepy.error.TweepError:
    	print "Error replying to @%s :(" % (sn)

set_enviados (PATH_FICHEIRO, enviados)


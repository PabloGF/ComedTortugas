#!/usr/bin/env python
import tweepy
import re
import random
from keys import keys
import serial
import commands
arduino = serial.Serial('/dev/ttyS0', 9600)
comando = 'H' #Input

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

PATH_LISTA="/home/debian/code/.tweets_enviados"
PATH_FOTO='/home/debian/code/tortugas.JPG'

def get_enviados (path):
        try:
                with open(path, "r") as archivo:
			return map(lambda x:int(x),archivo.readlines())
        except:
                return []

def set_enviados (path, lista):
	with open(path, "w") as archivo:
		 archivo.write("\n".join([str(x) for x in lista]))


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

enviados = get_enviados (PATH_LISTA)

tweets = api.search(q="comed, tortugas!")
tweets = [tweet for tweet in tweets if re.match("^comed,? tortugas!?$", tweet.text.lower())]
tweets = [tweet for tweet in tweets if tweet.id not in enviados]
random.shuffle(tweets)

output=commands.getoutput('sudo fswebcam -d /dev/video2 -r 640x480 %s' % (PATH_FOTO))

if tweets:
     arduino.write(comando)
     arduino.close()

for i,tweet in enumerate(tweets):
    sn = tweet.user.screen_name
    m1 = "[TEST] Gracinhas por darnos de comer, @%s! Se ves a @OSHWDem, agradeceremocho persoalmente!" % (sn)
    m2 = "[TEST] Parece que se che adiantaron, @%s! Proba nun cacho :)" % (sn)
    
    m = m2 if i else m1
    
    try:
	s = api.update_with_media(PATH_FOTO, m, tweet.id)
	enviados.append(tweet.id)
	print "Tweet replied to @%s :)" % (sn)
    except tweepy.error.TweepError as error:
	print "Error replying to @%s :(" % (sn)
	print error

set_enviados (PATH_LISTA, enviados)




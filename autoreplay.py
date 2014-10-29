#!/usr/bin/env python
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# f=open("kk.txt","w")
# f.write("machacando\n")
# f.close()
# f=open("kk.txt")
# f.read()
#'machacando\n'
# f.close()

twt = api.search(q="comed, tortugas!")

t = ['comed tortugas',
    'Comed Tortugas',
    'Comed tortugas',
    'comed Tortugas',
    'Comed tortugas!',
    'Comed, tortugas!']

for s in twt:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "[TEST] Gracias por darnos de comer, @%s! Si vienes a la @OSHWDem, te lo agradeceremos personalmente!" % (sn)
            s = api.update_status(m, s.id)

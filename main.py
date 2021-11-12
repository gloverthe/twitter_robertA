

#@santanderukhelp
from get_mentions import  get_tweets
from time import sleep
#from twitterSentinment import twitterSentiment
from robertA import *


def tweets_to_get():
    #user_ids = [962692878, 42664060, 943095541050892289, 517679199]
    get_tweets(962692878, 'Santander UK Help')
    get_tweets(42664060, 'Santander UK')
    get_tweets(943095541050892289, 'Santander UK News')
    get_tweets(517679199, 'SantanderUK Business')
    # twitterSentiment()
    robertA()
    #print(user_ids[1])


# tweets_to_get()

i=1
while i < 10:
    tweets_to_get()
    sleep(10)
    i=+1


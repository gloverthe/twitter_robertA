
import pandas as pd
import sqlite3
from sqlite3 import Error
from functions.sqlQueries import *
from functions.pubConstants import EnvConstants
from functions.sqlQueries import sqlliteQ
from functions.sqLiteFuncs import *
import pickle
from nltk.tokenize import word_tokenize
from functions.nlpFuncs import *
from twitter_roBERTa import twitterSentCardiff

def twitterSentiment():
    engine = sqliteConnect(EnvConstants.sqlDBPath)
    # c = engine.cursor()
    # c.execute('select max(id) as maxID from sanTweets where atUser = "' + atUser + '"')
    # maxId = c.fetchall()[0]
    try:
        noSent = pd.read_sql(sqlliteQ.getNoSent, engine)
        print(noSent)
        engine.close()
        classifier_f = open(os.path.join('pickle', 'my_classifier.pickle'), "rb")
        classifier = pickle.load(classifier_f)
        classifier_f.close()
        noSent['customTokens'] = noSent.apply(lambda row:  remove_noise(word_tokenize(row['text'])), axis = 1)
        noSent['sentiment'] = noSent.apply(lambda row:  classifier.classify(dict([token, True] for token in row['customTokens'])),axis = 1)
        del noSent['customTokens']
        print(noSent)
        print(noSent.describe())
        appendToSQLliteNoUser(noSent)
    except:
        print('No new records')


def twitterSentimentCardiff():
    engine = sqliteConnect(EnvConstants.sqlDBPath)
    # c = engine.cursor()
    # c.execute('select max(id) as maxID from sanTweets where atUser = "' + atUser + '"')
    # maxId = c.fetchall()[0]
    try:
        noSent = pd.read_sql(sqlliteQ.getNoSent, engine)
        print(noSent)
        engine.close()
        noSent['sentiment'] = noSent.apply(lambda row:  twitterSentCardiff(row['text']),axis = 1)
        print(noSent)
        print(noSent.describe())
        appendToSQLliteNoUser(noSent)
    except:
        print('No new records')

# engine = sqliteConnect(EnvConstants.sqlDBPath)
# noSent = pd.read_sql(sqlliteQ.getNoSent, engine)
# print(noSent)
# engine.close()
# noSent['sentiment'] = noSent.apply(lambda row:  twitterSentCardiff(row['text']),axis = 1)
# print(noSent)
# print(noSent.describe())
# appendToSQLliteNoUser(noSent)
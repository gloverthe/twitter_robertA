#create sqlite tables for san tweets

import sqlite3
from sqlite3 import Error

from functions.sqLiteFuncs import sqliteConnect
from functions.sqLiteFuncs import create_table

from functions.pubConstants import EnvConstants




all_tweets = """ CREATE TABLE IF NOT EXISTS sanTweets (
                                        created_at datetime,
                                        id text NOT NULL,
                                        text text
                                        atUser
                                    ); """

all_tweets_stg = """ CREATE TABLE IF NOT EXISTS stg_sanTweets (
                                        created_at datetime,
                                        id text NOT NULL,
                                        text text
                                    ); """

all_tweets_sent = """ CREATE TABLE IF NOT EXISTS sanTweetsSent (
                                        created_at datetime,
                                        id text NOT NULL,
                                        text text
                                        sentiment text
                                        intent text
                                    ); """


conn = sqliteConnect(EnvConstants.sqlDBPath)

# create tables
if conn is not None:
    # create all_tweets_table
    create_table(conn, all_tweets)
    create_table(conn, all_tweets_stg)
    create_table(conn, all_tweets_sent)

else:
    print("Error! cannot create the database connection.")
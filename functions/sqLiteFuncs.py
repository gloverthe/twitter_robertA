
import sqlite3
from sqlite3 import Error

from functions.pubConstants import EnvConstants
from functions.sqlQueries import sqlliteQ
import os

def sqliteConnect(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)




#create sqllie db

def create_db(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


'append tweets to table'
def appendToSQLlite(atUser, tweetDF):
    engine = sqliteConnect(EnvConstants.sqlDBPath)
    engine.execute('delete from stg_sanTweets')
    tweetDF.to_sql('stg_sanTweets', con=engine, if_exists='append')
    with engine as connection:
        connection.execute(sqlliteQ.insertToMain(atUser))
    engine.close()

# get max tweet id
def getMaxTweet(atUser):
    #returns the max tweet id to pass as a param to endpoint
    engine = sqliteConnect(EnvConstants.sqlDBPath)
    c = engine.cursor()
    c.execute('select max(id) as maxID from sanTweets where atUser = "' + atUser + '"')
    maxId = c.fetchall()[0]
    engine.close()
    return maxId[0]

def appendToSQLliteNoUser(tweetDF):
    engine = sqliteConnect(EnvConstants.sqlDBPath)
    engine.execute('delete from stg_sanTweetsSent2')
    tweetDF.to_sql('stg_sanTweetsSent2', con=engine, if_exists='append')
    with engine as connection:
        connection.execute(sqlliteQ.insertToSent)
    engine.close()



#if __name__ == '__main__':
#    create_connection(os.path.join('data', 'db', 'santweets.db'))
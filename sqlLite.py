
#from sqlalchemy import create_engine

from functions.sqLiteFuncs import sqliteConnect

from functions.pubConstants import EnvConstants

import sqlite3

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import query

import sqlalchemy as db

from functions.sqlQueries import sqlQ

# engine = sqliteConnect(EnvConstants.sqlDBPath)
# with engine as connection:
#     connection.execute(sqlQ.insertToMain('Santander UK Help'))


def getMaxTweet():
    engine = sqliteConnect(EnvConstants.sqlDBPath)
    c = engine.cursor()
    c.execute('select max(id) as maxID from sanTweets')
    maxid = c.fetchall()[0]
    return maxid[0]

print(getMaxTweet())




#sanTweetsTable = db.Table('sanTweets', metadata, autoload=True, autoload_with=engine)

#print(sanTweetsTable)

#maxID = db.select([db.func.sum(sanTweetsTable.columns.ID).lable('maxID')])



#Session = sessionmaker(bind=engine)


#session = Session()

# maxID = query('select max(id) as maxID from sanTweets', session = session)


#maxID = session.query('sanTweets').FUNCTION(max(id))
#print(maxID)
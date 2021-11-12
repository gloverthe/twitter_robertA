
class sqlliteQ:
    def insertToMain(atUser):
        insertToMain = '  insert or ignore into sanTweets (created_at, id, text, atUser)  select created_at, id, ' \
                        ' text, "' + atUser + '" as atUser from stg_sanTweets '
        return insertToMain

    getNoSent = 'select 	* from 	sanTweets where cast(id as "text")||atUser ' \
                '  not in ' \
                '(select DISTINCT cast(id as "text")||atUser from sanTweetsSent)'

    insertToSent = 'insert or ignore into sanTweetsSent (created_at, id, text, atUser, sentiment, intent)  select created_at, id, ' \
                        ' text, atUser, sentiment, "" as intent from stg_sanTweetsSent2'

#print(sqlQ.insertToMain('Santander UK Help'))


Testing the twitter API

Scripts will call the twitter timeline mentions API and load tweets menitoning user ids to a sqlite database



Twitter API docs:
https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-mentions
https://developer.twitter.com/en/docs/twitter-api/pagination

amazon comprehend
https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-dg.pdf#API_Reference



libraries
pip install sqlalchemy
pip install requests
pip install pandas


Nltk downloads for sentiment:
#in python command line
import nltk
nltk.download('twitter_samples')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')



{
    "data": [
        {
            "created_at": "2009-05-26T16:50:53.000Z",
            "description": "Information, news and updates about Santander UK. For service queries please contact @santanderukhelp",
            "id": "42664060",
            "name": "Santander UK",
            "username": "santanderuk"
        },
        {
            "created_at": "2012-11-21T16:39:43.000Z",
            "description": "We're here to help 8am - 8pm Mon-Fri, 9am - 5pm Saturday and Sunday. We'll never ask for account details or passwords. UK only.",
            "id": "962692878",
            "name": "Santander UK Help",
            "username": "santanderukhelp"
        },
        {
            "created_at": "2017-12-19T12:27:53.000Z",
            "description": "News and comment from the Santander UK Corporate Communications team, for customer queries please use @santanderukhelp.",
            "id": "943095541050892289",
            "name": "Santander UK News",
            "username": "santanderuknews"
        },
        {
            "created_at": "2012-03-07T15:13:40.000Z",
            "description": "Here to help your business prosper. For customer queries please contact @santanderukhelp",
            "id": "517679199",
            "name": "SantanderUK Business",
            "username": "santanderukbiz"
        }
    ]
}

Process finished with exit code 0

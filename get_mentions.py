import requests
import os
import json
import datetime
from datetime import datetime, timezone
import pandas as pd
# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
from sqlalchemy import create_engine

from functions.sqLiteFuncs import *

from functions.pubConstants import EnvConstants


from functions.constants import apiKeys
from functions.genFuncs import *
from functions.sqlQueries import sqlliteQ



# https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-mentions

def create_url(user_id):
    # Replace with user ID below
    #user_id = 962692878
    return "https://api.twitter.com/2/users/{}/mentions".format(user_id)




def get_params(atUser):
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at",
            "end_time": getStartTime(datetime.datetime.utcnow()),
            "start_time": getEndTime(datetime.datetime.utcnow()),
            'max_results': '100',
            'since_id': getMaxTweet(atUser)
            #"expansions": ''
             # "tweet.fields": 'geo.'
            }



    #datetime.datetime.now().isoformat()
    #>> > 2020 - 03 - 20T14: 28:23.382748
#endTime =  datetime.datetime.now().isoformat() - datetime.timedelta(minutes=nowMinusEnd)


#time format
#    YYYY - MM - DDTHH: mm:ssZ

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()



def get_tweets(user_id, atUser):
    #setup api request
    bearer_token = apiKeys.bearerToken
    url = create_url(user_id)
    headers = create_headers(bearer_token)
    params = get_params(atUser)
    paginationNext = ''
    print(params)
    i = 0
    end = 0
    if i == 0:
        json_response = connect_to_endpoint(url, headers, params)
        print(json.dumps(json_response, indent=4, sort_keys=True))
        #print(connect_to_endpoint()).text
        if json_response['meta']['result_count'] > 0:
            sanTweets = pd.json_normalize(json_response['data'])
            print(sanTweets)
            print(sanTweets.describe())
            try:
                paginationNext = json_response['meta']['next_token']
            except:
                end == 0
            print("Pagenation Token : " + paginationNext)
            appendToSQLlite(atUser= atUser, tweetDF= sanTweets)
        i =+1
    elif i > 0:
        while end == 0:
            params["pagination_token"] = paginationNext
            if json_response['meta']['result_count'] > 0:
                json_response = connect_to_endpoint(url, headers, params)
                print(json.dumps(json_response, indent=4, sort_keys=True))
                sanTweets = pd.json_normalize(json_response['data'])
                print(sanTweets)
                print(sanTweets.describe())
                appendToSQLlite(atUser=atUser, tweetDF=sanTweets)
                try:
                    paginationNext = json_response['meta']['next_token']
                except:
                    end == 0
                print("Pagenation Token : " + paginationNext)
        print('end')









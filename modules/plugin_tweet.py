#coding: utf-8

import urllib
import json

url = "http://search.twitter.com/search.json?%s"

def get_tweets(key):
    params = dict(q=key, result_type='mixed', count=3)
    response = urllib.urlopen(url % urllib.urlencode(params))
    tweets = json.loads(response.read())
    return tweets

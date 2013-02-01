# coding: utf-8

from plugin_tweet import get_tweets

def index():
    key = request.vars.key
    tweets = get_tweets(key)
    logger.info(tweets.keys())
    return dict(tweets=tweets)

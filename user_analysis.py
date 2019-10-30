from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream, API, Cursor
import credentials
from auth import TwitterAuthenticator
from twitter_client import TwitterClient
from analyser import TweetAnalyser
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from textblob import TextBlob
import re


if __name__ == "__main__":
    tweet_analyser = TweetAnalyser()
    twitter_client = TwitterClient()
    api = twitter_client.get_twitter_client_api()

    # stream tweets
    tweets = api.user_timeline(screen_name = "eminem", count = 200)
    # print(dir(tweets[0]))

    df = tweet_analyser.tweets_to_data_frame(tweets)
    df["sentiment"] = np.array([tweet_analyser.analyse_sentiment(tweet) for tweet in df["tweets"]])
    print(df.head(10))

    # # getting avaeage length of all tweets
    # print(round(np.mean(df["len"])))
    # print(np.max(df["likes"]))
    # print(np.max(df["retweets"]))

    time_likes = pd.Series(data=df["likes"].values, index=df["date"])
    time_likes.plot(figsize=(16, 4), label="likes", legend=True)
    time_retweets = pd.Series(data=df["retweets"].values, index=df["date"])
    time_retweets.plot(figsize=(16, 4), label="retweets", legend=True)
    plt.show()
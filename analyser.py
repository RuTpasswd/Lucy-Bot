from textblob import TextBlob
import re
import numpy as np
import pandas as pd

class TweetAnalyser:
    """
    Functionality for analysing and categorizing content from tweets
    """
    def clean_tweet(self, tweet):
        return " ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyse_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))

        # check if tweet is positve or negative
        if analysis.sentiment.polarity > 0:
            return 1 #positive
        elif analysis.sentiment.polarity == 0:
            return 0 #neutral
        else:
            return -1 #negative

    def tweets_to_data_frame(self, tweets):
        data_frame = pd.DataFrame(data = [tweet.text for tweet in tweets], 
                                  columns = ["tweets"])

        data_frame["id"] = np.array([tweet.id for tweet in tweets])
        data_frame["len"] = np.array([len(tweet.text) for tweet in tweets])
        data_frame["date"] = np.array([tweet.created_at for tweet in tweets])
        data_frame["likes"] = np.array([tweet.favorite_count for tweet in tweets])
        data_frame["retweets"] = np.array([tweet.retweet_count for tweet in tweets])
        data_frame["source"] = np.array([tweet.source for tweet in tweets])
        
        return data_frame
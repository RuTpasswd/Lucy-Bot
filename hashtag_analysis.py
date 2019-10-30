from auth import TwitterAuthenticator
from tweepy.streaming import StreamListener
from tweepy import Stream
from analyser import TweetAnalyser

# creation of class which inherits from the StreamListener class
class TwitterListener(StreamListener):
    """
    Basic listener class which prints received tweets
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    # takes in streamed data
    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, "a") as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print(f"Error on data {e}")
        return True

   
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

    # handles errors
    def on_error(self, status):
        if status == "420":
            # returning false incase rate limit is reached
            return False

# class for streaming the tweets based on our needs
class TwitterStreamer:
    """
    class for streaming and processing live tweets
    """

    # instantiateing the auth class
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
    # function to catch streamed tweets
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):   
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter() 
        stream = Stream(auth, listener)

        # to filter the stream
        stream.filter(track=hash_tag_list)

if __name__ == "__main__":
    # how do I deal with the data
    hash_tag_list = ["Arsenal", "Xhaka", "Emery"]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
from auth import TwitterAuthenticator
from tweepy.streaming import StreamListener
from tweepy import Stream
from analyser import TweetAnalyser

# creation of class which inherits from the StreamListener class
class TwitterListener(StreamListener):
    """
    Basic listener class which prints received tweets
    """
   
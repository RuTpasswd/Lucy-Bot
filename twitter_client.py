from tweepy import Cursor, API


# twitter client
class TwitterClient:
    """
    Class to get data from twitter
    """
    def __init__(self, twitter_user = None):
        self.auth = TwitterAuthenticator().authenticate_twitter()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user
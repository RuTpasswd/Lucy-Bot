from tweepy import Cursor, API
from auth import TwitterAuthenticator

# twitter client
class TwitterClient:
    """
    Class to get data from twitter
    """
    def __init__(self, twitter_user = None):
        self.auth = TwitterAuthenticator().authenticate_twitter()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client
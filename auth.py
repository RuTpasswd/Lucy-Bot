import credentials
from tweepy import OAuthHandler

# class for authentication
class TwitterAuthenticator:
    """
    Facilitates authentication
    """
    def authenticate_twitter(self):
        """
        Authentication to connect to the Twitter API
        """
        auth = OAuthHandler(credentials.CONSUMER_KEY,
                            credentials.CONSUMER_SECRET)
        auth.set_access_token(credentials.ACCESS_TOKEN,
                            credentials.ACCESS_TOKEN_SECRET)
        return auth
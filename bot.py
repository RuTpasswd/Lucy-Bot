import tweepy
import time
from auth import TwitterAuthenticator
import json
from difflib import get_close_matches
import requests

print('I AM A BOT', flush=True)

authenticator = TwitterAuthenticator()
auth = authenticator.authenticate_twitter()
api = tweepy.API(auth)
handle = open("data.json")
data = json.load(handle)
response = requests.get("https://api.kanye.rest/").json()

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        mention_list = mention.full_text.lower().split(" ")
        print(mention.full_text.lower())
        if mention_list[2] == "#dict":
            print('found #dict!', flush=True)
            print('responding back...', flush=True)

            word = mention_list[3]
            close = get_close_matches(word, data.keys(), cutoff=0.7)
            if word in data:
                for w in data[word]:
                    api.update_status('@' + mention.user.screen_name +
                    " " + w, mention.id)
            elif len(close) > 0:
                api.update_status('@' + mention.user.screen_name +
                    "Oops, did you mean {} instead?".format(close[0]), mention.id)
            else:
                api.update_status('@' + mention.user.screen_name +
                    "Didn't quite get that, sorry", mention.id)
        
        elif mention_list[2] == "#meme":
            print('found #dict!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    " Your mum gei", mention.id)

        elif mention_list[2] == "#kanye" or mention_list[2] == "#kanyewest" or mention_list[2] == "#ye":
            print('found match!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    " " + response["quote"] + " - Kanye West", mention.id)

          
while True:
    reply_to_tweets()
    time.sleep(20)
import tweepy
import time
from auth import TwitterAuthenticator
import json
from difflib import get_close_matches
import requests
import random
import os

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
    last_seen_id = int(float(f_read.read().strip()))
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
        if mention_list[1] == "#dict":
            print('found #dict!', flush=True)
            print('responding back...', flush=True)
            word = mention_list[2]
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
        
        if mention_list[1] == "#kanye" or mention_list[1] == "#kanyewest" or mention_list[1] == "#ye":
            print('found match!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    " " + response["quote"] + " - Kanye West", mention.id)

        if mention_list[1] == "#help":
            print('found help!')
            print('responding...')
            api.update_status('@' + mention.user.screen_name + 
                        "  Hello, my commands are #dict plus a word for its definition and #kanye for a random @kanyewest quote. Have fun",
                        mention.id)

        # if mention_list[1] == "#meme" or mention_list[1] == "#memes":
        #     print('found #meme')
        #     print('responding...')
        #     os.chdir('memes')
        #     images = os.listdir('.')
        #     index = random.randint(0,20)
        #     api.update_with_media(images[index], '@' + mention.user.screen_name)

        
while True:
    reply_to_tweets()
    time.sleep(20)
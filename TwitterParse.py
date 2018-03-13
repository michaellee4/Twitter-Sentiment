import tweepy
import time
import ProcessTweet
from CalcSentiment import SentimentAnalyzer
import string

# Api key info
consumer_key = 'Your key'
consumer_secret = 'Your secret'
access_token = 'Your token'
access_token_secret = 'Your token'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True

api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if (not status.retweeted) and ('RT @' not in status.text) and ('https://' not in status.text):
            tweet = ProcessTweet.clean(status.text)
            analyzer = SentimentAnalyzer()
            sent_dict = analyzer.polarity_scores(tweet)
            compound = float(sent_dict.get('compound'))
            print(compound)
            #print (tweet)

    def on_error(self, status_code):
        if status_code == 420:
            print("Temporary Limit Exceeded")
            return False


def tweetStream(list_of_filters, duration):
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(languages=['en'], track=list_of_filters, async=True)
    time.sleep(duration)
    myStream.disconnect()

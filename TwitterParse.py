import tweepy
import time
import ProcessTweet
from CalcSentiment import SentimentAnalyzer
import string

# Api key info
#Enter your informatino here
consumer_key = 'Your key'
consumer_secret = 'Your secret'
access_token = 'Your token'
access_token_secret = 'Your token'

#Oauth process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True

api = tweepy.API(auth)

#Stream listener class that reads in tweets for analysis
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if (not status.retweeted) and ('RT @' not in status.text) and ('https://' not in status.text):
            tweet = ProcessTweet.clean(status.text)
            analyzer = SentimentAnalyzer()
            sent_dict = analyzer.polarity_scores(tweet)
            compound = float(sent_dict.get('compound'))
            #Redirect this output
            print(compound)
            #print (tweet)

#420 is the error number for exceeding your limit as allowed by the api
    def on_error(self, status_code):
        if status_code == 420:
            print("Temporary Limit Exceeded")
            return False

#Driver function that creates a tweet stream and leaves it open for a set amount of time
def tweetStream(list_of_filters, duration):
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(languages=['en'], track=list_of_filters, async=True)
    time.sleep(duration)
    myStream.disconnect()

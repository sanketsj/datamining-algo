#in order to learn data mining with python
import tweepy
from textblob import TextBlob as tb 

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('#MeTooIndia')

for tweet in public_tweets:
	print(tweet.text)
	analysis = tb(tweet.text)
	print(analysis.sentiment)



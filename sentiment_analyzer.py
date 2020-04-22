import tweepy
from textblob import TextBlob


consumer_key = 'SgJJpWvvQMB0QU2nrRM6by2DM'
consumer_key_secret = '8aRUfDlqzuoOnY5yaGrcwkStVqoDvxo6aTutXM8LlNfkG0BUZz'

access_token = '784635562946887681-Gc2iiIEa8QCMxSX9fIUClBARsTBGXdo'
access_token_secret = 'zbBip5pTugOsMtXlZtGVxlnf8mgEOFlOoJFhLqk2HzlAX'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search_term = input("Enter a search keyword: ")
public_tweets = api.search(search_term)



for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	if analysis.sentiment[0]>0:
		print ('Positive')
	else:
		print ('Negative')
	print("")
from django.shortcuts import render
import tweepy

from .forms import TweetForm

# Create your views here.

def index(request):
	return render(request, 'index.html')

def home(request):
	consumer_key =" "
	consumer_secret = " "

	key = " "
	secret = " "

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(key, secret)

	if request.method == "POST":
		Mypost = request.POST['MyTweet']

		api = tweepy.API(auth)
		api.update_status(Mypost)

	public_tweets = api.home_timeline()


def get_trends(request):
    consumer_key = " "
    consumer_secret = " "
    access_token = " "
    access_token_secret = " "

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    woeid = 2459115 # New York, USA

    trends = api.trends_place(woeid)[0]["trends"][:10]

    trend_names = [trend["name"] for trend in trends]
    
    return HttpResponse(trend_names)

def get_tweets(request):
    consumer_key = ""
    consumer_secret = ""
    access_token = " "
    access_token_secret = " "

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    # Set the number of tweets you want to fetch
    num_tweets = 10

    # Fetch the tweets
    tweets = api.user_timeline(count=num_tweets)

    # Create a list to hold the tweet texts
    tweet_texts = []

    # Loop through the tweets and append the text to the list
    for tweet in tweets:
        tweet_texts.append(tweet.text)

    # Return the tweet texts as a response
    return render(request, 'tweets.html', {'tweets': tweet_texts})
#This will not run because of Elon Musk buying Twitter, but its for practice
import tweepy #twitter and python's module to interact with the API
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #these are for your api keys
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline() #this pulls the home_timeline in your browser like when you login to Facebook
for tweet in public_tweets:
    print(tweet.text)

user = api.me
print(user.name) #would show twitter username

def limit_handler(cursor): #this will help so you don't crash the servers at Twitter from spanning them
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

#Super Genrous Bot will follow back followers
for follower in limit_handler(tweepy.Cursor(api.follwers).items()):
    if follower.name == 'John':
        follower.follow()
        break

#Narsists Bot 
search_string = 'Ryan'
numberOfTweets = 5

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

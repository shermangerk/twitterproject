import tweepy

consumer_key = "xxxx"
consumer_secret = "xxxx"

access_token = "xxxx"
access_token_secret = "xxxx"

#creating authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
name = "nytimes"
tweetCount = 500
results = api.user_timeline(id=name,count=tweetCount)
i=1

for tweet in results:
    print("tweet " + str(i) + "- Account Name: " + tweet.user.screen_name)
    print("content " + tweet.text)
    i= i+1
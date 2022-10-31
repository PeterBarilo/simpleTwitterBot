import tweepy
import time

auth = tweepy.OAuthHandler(
    'API KEY', 'API KEY SECRET', )
auth.set_access_token(
    'Acces Token', 'Access Token Secret'
)

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            try:
                yield next(cursor)
            except StopIteration:
                return
    except tweepy.RateLimitError:
        time.sleep(1000)


search_string = '[ITEM TO SEARCH FOR]'
numberOfTweets = 5

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('done')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

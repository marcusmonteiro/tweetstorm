import tweepy
import nltk
import sys
from os import getenv


def get_environment_variable(environment_variable_name):
  ''' Returns an environment variable's value or raises an error'''
  key = getenv(environment_variable_name)
  if not key:
    raise LookupError('Please set the {} environment variable'.format(environment_variable_name))
  return key


def get_tweepy_api():
  consumer_key = get_environment_variable('TWITTER_CONSUMER_KEY')
  consumer_secret = get_environment_variable('TWITTER_CONSUMER_SECRET')
  access_token = get_environment_variable('TWITTER_ACCESS_TOKEN')
  access_token_secret = get_environment_variable('TWITTER_ACCESS_TOKEN_SECRET')

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  return tweepy.API(auth)


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def break_into_tweets(text):
  if not text:
    raise ValueError("Parameter `text` is empty")
  try:
    nltk.data.find('tokenizers/punkt/english.pickle')
  except LookupError:
    nltk.download('punkt')

  sentences = nltk.tokenize.sent_tokenize(text)
  tweets = []
  character_limit = 140
  sequential_prefix_template = '1/'
  character_limit_minus_prefix_size = character_limit - len(sequential_prefix_template)
  i = 1
  for sentence in sentences:
    chunks = chunker(sentence, character_limit_minus_prefix_size)
    prepared_tweets = []
    for chunk in chunks:
      prepared_tweets.append('{}/{}'.format(i, chunk).rstrip())
      i = i + 1
    tweets.extend(prepared_tweets)

  return tweets


if __name__ == '__main__':
  filename = sys.argv[1]
  try:
    with open(filename) as f:
      text = f.read()
  except FileNotFoundError:
    text = filename

  tweets = break_into_tweets(text)
  api = get_tweepy_api()
  for tweet in tweets:
    api.update_status(tweet)


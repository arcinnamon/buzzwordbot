import random
import requests
import tweepy
import os

# declare lists
nouns = []
verbs = []
phrases = []

# load nouns, verbs, and phrases from files
nounList = open('nouns.txt', 'r')
for nounLine in nounList:
    nouns.append(nounLine)
nounList.close()

verbList = open('verbs.txt', 'r')
for verbLine in verbList:
    verbs.append(verbLine)
verbList.close()

phraseList = open('phrases.txt', 'r')
for phraseLine in phraseList:
    phrases.append(phraseLine)
phraseList.close()

# select random noun, verb, and phrase
randomNoun = random.choice(nouns).replace("\n","")
randomVerb = random.choice(verbs).replace("\n","")
randomPhrase = random.choice(phrases)

# replace [verb] with randomVerb and replace [noun] with randomNoun
replaceNoun = randomPhrase.replace("[noun]", randomNoun)
replaceVerb = replaceNoun.replace("[verb]", randomVerb)

# output
print(replaceVerb)

# tweepy module ############################

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : open('consumer_key.txt', 'r'),
    "consumer_secret"     : open('consumer_secret.txt', 'r'),
    "access_token"        : open('access_token.txt', 'r'),
    "access_token_secret" : open('access_token_secret.txt', 'r')
    }

  api = get_api(cfg)
  tweet = replaceVerb
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()

############################################
  
# TO-DO
# a/an
# adjectives
# multiple/different nouns/verbs in a single phrase
import random
import requests
import tweepy

# declare lists
nouns = []
verbs = []
phrases = []

# load nouns, verbs, and phrases from files
nounList = open('/home/ec2-user/buzzwordbot/nouns.txt', 'r')
for nounLine in nounList:
    nouns.append(nounLine)
nounList.close()

verbList = open('/home/ec2-user/buzzwordbot/verbs.txt', 'r')
for verbLine in verbList:
    verbs.append(verbLine)
verbList.close()

phraseList = open('/home/ec2-user/buzzwordbot/phrases.txt', 'r')
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
# print(replaceVerb)

# tweepy module ############################

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "Vj174tDvH05i4PQIPldNNylsz",
    "consumer_secret"     : "XMEbeHQK6jrdRzESKkTmRuElyxTQSBFEnAk0eDfIigoT01KwJ6",
    "access_token"        : "914614650658017282-KFEKavrhoMO48mSOPj6HqK5W4z0EB2s",
    "access_token_secret" : "p4FXmVEcszxr2I0Q554c4AVGAIqEEugUm95nvh6beLWOT" 
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

import requests
from bs4 import BeautifulSoup as bs
import re
import tweepy

url = "http://www.espn.com/nba/"
page = requests.get(url)
soup = bs(page.text, 'html.parser')

tags = soup.find_all("a", href=re.compile("lebron", re.IGNORECASE))

# Formatting the LeBron references:
links = []
for tag in tags:
  link = tag["href"]
  if (link[0] == "/"):
    link = "http://www.espn.com" + link
  links.append(link)

links = set(links)
#for link in links:
#  print(link)
'''
auth = tweepy.OAuthHandler("4EIzGMER6zRRHUmDOfBKZ1bRT", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

'''
print(len("4EIzGMER6zRRHUmDOfBKZ1bRT"))
print(len("5GAVXHDRYRrWeeFhQGyU3SJhomZdJjP3fEqL7jt94JUsYRrfZ4"))
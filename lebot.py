import requests
from bs4 import BeautifulSoup as bs
import re
from TwitterAPI import TwitterAPI
import config
import time

# URL for web scraping the keyboard 'lebron'
url = "http://www.espn.com/nba/"
# Dictionary/hashtable for keeping track of which links were already posted to Twitter 
used_links = {}

def get_lebron_links():
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

  return links

def post_to_twitter(link):
  api = TwitterAPI(config.api_key, config.api_secret, config.access_token, config.access_token_secret)
  r = api.request("statuses/update", {"status": link})

# Request web scraping data from ESPN every 15 seconds
while (True):
  links = get_lebron_links()
  for link in links:
    if (link not in used_links):
      used_links[link] = True
      post_to_twitter(link)
  time.sleep(15)
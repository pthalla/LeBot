import requests
from bs4 import BeautifulSoup as bs
import re
from TwitterAPI import TwitterAPI
import config
import time

url = "http://www.espn.com/nba/"

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
  links = list(set(links))
  
  return links
  

'''
def post_to_twitter(links):
  api = TwitterAPI(config.api_key, config.api_secret, config.access_token, config.access_token_secret)
  r = api.request("statuses/update", {"status": links[0]})
  print(r.status_code)
'''


while (True):
  links = get_lebron_links()
  for link in links:
    print(link)
  time.sleep(2)
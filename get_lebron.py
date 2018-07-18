import requests
from bs4 import BeautifulSoup as bs
import re
from TwitterAPI import TwitterAPI
import config

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

api = TwitterAPI(config.api_key, config.api_secret, config.access_token, config.access_token_secret)
r = api.request("statuses/update", {"status": "This is from my python!"})
print(r.status_code)
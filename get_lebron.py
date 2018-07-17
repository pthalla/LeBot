import requests
from bs4 import BeautifulSoup as bs
import re

def find_lebron():
  print("found")

url = "http://www.espn.com/nba/"

page = requests.get(url)
soup = bs(page.text, 'html.parser')

#output = soup.find_all(text="LeBron")
#output = soup.body.findAll(text=re.compile('LeBron'))
output = soup.find_all(string=re.compile("LeBron"))
for title in output:
  print(title)
#print(output)


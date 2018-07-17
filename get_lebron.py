import requests
from bs4 import BeautifulSoup as bs

url = "http://www.espn.com/nba/"

page = requests.get(url)
soup = bs(page.text, 'html.parser')

output = soup.find_all(text="LeBron")
print(output)
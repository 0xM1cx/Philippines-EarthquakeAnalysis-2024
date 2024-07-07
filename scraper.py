import requests
from bs4 import BeautifulSoup

URL = "https://earthquaketrack.com/p/philippines/recent"
#URL = "https://earthquake.phivolcs.dost.gov.ph/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
print(soup)

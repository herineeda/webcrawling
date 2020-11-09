import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://www.daangn.com/hot_articles")
soup = BeautifulSoup(webpage.content, "html.parser")

# print(soup)

# print(soup.p)

# print(soup.p.string)

# print(soup.h1)

# print(soup.find_all("h2"))

# result = soup.find_all(attrs={'class':'card-title'})

# print(result)

# result = soup.select(".card-region-name")

# print(result)
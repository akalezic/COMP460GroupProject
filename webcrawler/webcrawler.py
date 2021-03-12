#Python file where webcrawler will be put to scrape the internet for search engine
import requests
from bs4 import BeautifulSoup

#get url of website you want to scrape
url = 'https://www.cnn.com/'
# uses requests to get website
page = requests.get(url)

soup = BeautifulSoup(page.content, 'lxml')
#currently struggling to get this to work
article = soup.find('h3')
headline = article.span.text
print(headline)
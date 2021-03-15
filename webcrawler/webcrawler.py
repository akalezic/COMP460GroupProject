# Python file where webcrawler will be put to scrape the internet for search engine
import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import io
import os

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)


class Crawler:
    count = 0

    def __init__(self, urls=[]):
        self.visited_urls = []
        self.urls_to_visit = urls

    def download_url(self, url):
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url):
        # count increments every new page is crawled
        self.count += 1
        # it is set to less than 10 so only 10 pages are downloaded
        if self.count < 12:
            # extracting only the domain for setting it to the file name
            # as file name cannot contain characters line '/' and '?'
            html = self.download_url(url)
            url_domain = url[8:]
            save_path = "./crawledPages"
            url_domain = url_domain.replace('?', '')
            domain = []
            domain = url_domain.split('/')

            # extracting text from html
            soup = BeautifulSoup(html)
            for script in soup(["script", "style"]):
                script.decompose()

            strips = list(soup.stripped_strings)

            # creating a file for the crawled page
            if domain[1] == "":
                file_name = domain[0] + '.txt'
            else:
                file_name = domain[0] + "-" + domain[1] + '.txt'

            complete_name = os.path.join(save_path, file_name)
            with io.open(complete_name, "w", encoding="utf-8") as f:
                for text in strips:
                    f.write(text)
                f.close()

            # finding and adding urls in the crawled page
            for url in self.get_linked_urls(url, html):
                self.add_url_to_visit(url)

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)


if __name__ == '__main__':
    Crawler(urls=['https://www.cnn.com/']).run()

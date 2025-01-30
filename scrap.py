import requests
from bs4 import BeautifulSoup

class Scrap:
    def __init__(self, url):
        self.url = url
        self.soup = self.scrap()

    def scrap(self):    
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(self.url,headers=headers)

        soup = BeautifulSoup(data.text, 'html.parser')
        return soup
    
    def url_image(self):
        url_image = self.soup.select_one('meta[property="og:image"]')['content']
        return url_image

    def url_title(self):
        url_title = self.soup.select_one('meta[property="og:title"]')['content']
        return url_title

    def url_description(self):
        url_description = self.soup.select_one('meta[property="og:description"]')['content']
        return url_description

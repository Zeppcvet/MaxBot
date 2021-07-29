import urllib.request
from bs4 import BeautifulSoup

class BestChange:
    def __init__(self, url):

        self.url = url

    def rate(self):

        html = urllib.request.urlopen(self.url).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup.find_all('td', attrs={'class': 'bi'})
        result = tags[1].text.strip()
        return result
    def print_rate(self):
        if __name__ == "__main__":
          answer = BestChange()
          return answer.rate()
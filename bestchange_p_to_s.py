import urllib.request
from bs4 import BeautifulSoup

url_p_to_s = "https://www.bestchange.ru/privat24-uah-to-sberbank.html"
url_s_to_p = "https://www.bestchange.ru/sberbank-to-privat24-uah.html"
url_s_to_m = "https://www.bestchange.ru/sberbank-to-monobank.html"
tag_class1 = 'bi'
tag_class2 = 'fs'
index1 = 1
index2 = 0
tag_name1 = 'td'
tag_name2 = 'div'

class BestChange:

    def __init__(self, url):
        self.url = url

    def rate(self, index, tag_name, tag_class):
        self.tag_name = tag_name
        self.tag_class = tag_class
        self.index = index
        html = urllib.request.urlopen(self.url).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup.find_all(str(tag_name), attrs={'class': str(tag_class)})
        result = tags[index].text.strip()
        return result

    def print_rate(self):
        if __name__ == "__main__":
            # noinspection PyArgumentList
            answer = BestChange(self.url).rate()
            return answer


# my_reply1 = BestChange(url_p_to_s).rate(index1, tag_name1, tag_class1)
# print(my_reply1)
#
# my_reply2 = BestChange(url_s_to_p).rate(index2,tag_name2,tag_class2)
# print (my_reply2)
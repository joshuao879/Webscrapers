import requests
result = requests.get("https://en.wikipedia.org/wiki/Tiger_Woods")

import bs4

soup = bs4.BeautifulSoup(result.text,"lxml")
name = soup.select('.toctext')[0]
#print(name.text)

for item in soup.select('.toctext'):
    print(item.text)

# name = soup.select('title')[0].getText()
# print(name)
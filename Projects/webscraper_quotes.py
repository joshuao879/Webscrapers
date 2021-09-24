import requests
import bs4

#AUTHORS

#----------------------------------------------

# base_url = 'https://quotes.toscrape.com/page/1/'

# authors = []

# result = requests.get(base_url)
# soup = bs4.BeautifulSoup(result.text,"lxml")
# author = soup.select('.author')[0].getText()

# for item in soup.select('.author'):
#     name = item.text
#     authors.append(name)

# print(authors)

#----------------------------------------------

#QUOTES

# base_url = 'https://quotes.toscrape.com/page/1/'

# result = requests.get(base_url)
# soup = bs4.BeautifulSoup(result.text,"lxml")

# for quote in soup.select('.text'):
#     print(quote.text)

#----------------------------------------------

#TOP TEN TAGS

# base_url = 'https://quotes.toscrape.com/page/1/'

# result = requests.get(base_url)
# soup = bs4.BeautifulSoup(result.text,"lxml")

# for quote in soup.select('.tag-item'):
#     print(quote.text)

#----------------------------------------------

#AUTHORS FROM ALL PAGES

base_url = 'https://quotes.toscrape.com/page/{}/'

authors = set()

while True:
    i = 1
    scrape_url = base_url.format(i)
    result = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(result.text,"lxml")

    if "No quotes found!" in result.text:
        print(authors)  
        break

    for item in soup.select('.author'):
        authors.add(item.text)
        
    i = i + 1


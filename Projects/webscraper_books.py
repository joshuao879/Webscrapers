#Get every title with two star rating

import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

two_stars = []
for n in range(1,51):
    scrape_url = base_url.format(n)
    result = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(result.text,"lxml")
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select('a')[1]['title']
            two_stars.append(book_title)

print(two_stars)
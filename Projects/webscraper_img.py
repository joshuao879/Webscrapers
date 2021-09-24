import requests
result = requests.get("https://en.wikipedia.org/wiki/Tiger_Woods")

import bs4

soup = bs4.BeautifulSoup(result.text,"lxml")
name = soup.select('.thumbimage')[0]
#print(name['src'])

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Tiger_and_Earl_Woods_Fort_Bragg_2004.jpg/220px-Tiger_and_Earl_Woods_Fort_Bragg_2004.jpg')

#Change below to save to somewhere other than vscode
f = open('tiger_woods.jpg', 'wb')
f.write(image_link.content)
f.close()
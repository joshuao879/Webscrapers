import requests
import bs4


result = requests.get("https://www.pgatour.com/stats/stat.101.html")
soup = bs4.BeautifulSoup(result.text,"lxml")

data = []

# name = soup.select('.player-name')
# print(name.text)

numbers = soup.find_all('div',class_= '.player-name')
print(numbers)

# for i in numbers:
#     td = i.find('td')
#     data.append(td.string)

# for item in soup.select('.player-name'):
#     name = item.text
#     data.append(name)

# print(data)


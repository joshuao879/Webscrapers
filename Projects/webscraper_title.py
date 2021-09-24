import requests
result = requests.get("http://www.example.com")
import bs4

soup = bs4.BeautifulSoup(result.text,"lxml")
name = soup.select('title')[0].getText()
print(name)



#from bs4 import BeautifulSoup
#import requests

#the following is for a html file
#with open('simple.html')
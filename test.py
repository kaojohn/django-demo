import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.yahoo.com.tw")
soup = BeautifulSoup(url, "lxml")

print(a)

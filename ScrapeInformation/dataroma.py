import requests
from lxml import html
from bs4 import BeautifulSoup as BS
from html.parser import HTMLParser
from json import loads
import re

url = "https://www.dataroma.com/m/home.php"

def get_page_source_code(url):

    header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.3"}
    response = requests.get(url, headers=header)
    soup = BS(response.content, "html.parser")
    return soup

def get_nasdaq_futures():
    soup = get_page_source_code(url)
    stocks = soup.find_all(
        "a")
    for x in stocks:
        print(x.text)

get_nasdaq_futures()
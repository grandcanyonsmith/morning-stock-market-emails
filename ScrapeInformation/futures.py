import requests
from lxml import html
from bs4 import BeautifulSoup as BS
from html.parser import HTMLParser
from json import loads


url = "https://www.cnn.com/business/markets/premarkets"


def get_page_source_code(url):

    header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.3"}
    response = requests.get(url, headers=header)
    soup = BS(response.content, "html.parser")
    return soup


def get_nasdaq_futures():

    soup = get_page_source_code(url)
    nasdaq_futures = soup.select_one(
        ".futureWrapper~ .futureWrapper+ .futureWrapper .jBluap+ .dWmdTT").get_text(strip=True)
    print(f"Nasdaq futures: {nasdaq_futures}")
    number_extract = nasdaq_futures[:-1]
    number_extract = float(number_extract)
    if number_extract < 0:
        negative_or_positive = 'negative'
    else:
        negative_or_positive = 'positive'
        nasdaq_futures = "+" + nasdaq_futures
    return nasdaq_futures, negative_or_positive


def get_dow_futures():
    try:

        soup = get_page_source_code(url)
        dow_futures = soup.select_one(".jBluap + .ThspH").get_text(strip=True)
        print(f"Dow futures: {dow_futures}")
        number_extract = dow_futures[:-1]
        number_extract = float(number_extract)
        if number_extract < 0:
            negative_or_positive = 'negative'
        else:
            negative_or_positive = 'positive'
            dow_futures = "+" + dow_futures
        return dow_futures, negative_or_positive
    except:
        Exception
        dow_futures = "-" + "0.00%"
        negative_or_positive = 'negative'
        return dow_futures, negative_or_positive


def get_spy_futures():

    soup = get_page_source_code(url)
    spy_futures = soup.select_one(
        ".futureWrapper:nth-of-type(3) .jBluap+ .dWmdTT").get_text(strip=True)
    print(f"Spy futures: {spy_futures}")
    number_extract = spy_futures[:-1]
    number_extract = float(number_extract)
    if number_extract < 0:
        negative_or_positive = 'negative'
    else:
        negative_or_positive = 'positive'
        spy_futures = "+" + spy_futures
    return spy_futures, negative_or_positive

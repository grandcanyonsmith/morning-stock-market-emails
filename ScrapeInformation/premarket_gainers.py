import json
from bs4 import BeautifulSoup
from requests import get
import requests
from lxml import html
from bs4 import BeautifulSoup as BS
from html.parser import HTMLParser
from json import loads
# from economic_data import econ_data


def get_page_source_code(url):

    header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.3"}
    response = requests.get(url, headers=header)
    return BS(response.content, "html.parser")


soup = get_page_source_code(
    'https://www.marketwatch.com/tools/screener/premarket')
top_three_tickers = []
difference = []
exchange_list = []

premarket_gainers_ticker = soup.find_all(
    'div', class_="cell__content fixed--cell")

premarket_gainers_change = soup.find_all(
    'li', class_="content__item value ignore-color")


# total_tickers = len(premarket_gainers_change)
def print_gainers():
    print("Biggest Pre-market Gainers")
    for i in range(3):
        if "-" not in premarket_gainers_change[i].text:
            print(premarket_gainers_ticker[i+1].text,
                  premarket_gainers_change[i].text)
            tick = premarket_gainers_ticker[i+1].text.strip()
            top_three_tickers.append(
                premarket_gainers_ticker[i+1].text.strip())
            difference.append(premarket_gainers_change[i].text)
    print(" ")
    print(" ")
    print(" ")
    print("Biggest Pre-market Losers")

    return top_three_tickers, difference


try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

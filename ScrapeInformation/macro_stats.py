from lxml import html
import requests
from bs4 import BeautifulSoup as BS




def get_tnx_week_diff():
    url = "https://www.marketwatch.com/investing/index/tnx?countrycode=xx"
    header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.3"}
    response = requests.get(url, headers=header)
    soup = BS(response.content, "html.parser")
    premarket_gainers_ticker = soup.find(
    'li', class_="content__item value ignore-color")
    ticker_price = soup.find_all(
    'span', class_="primary")
    ticker_price = ticker_price[1].text
    ticker_price = (float(ticker_price)/10).__round__(2)
    gainer= premarket_gainers_ticker.text
    tnx_gainer = float(gainer[:-1])
    print("TNX: ",tnx_gainer,"%")
    return tnx_gainer, ticker_price

def get_dyx_week_diff():
    url = "https://www.marketwatch.com/investing/index/dxy"
    header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.3"}
    response = requests.get(url, headers=header)
    soup = BS(response.content, "html.parser")
    premarket_gainers_ticker = soup.find(
    'li', class_="content__item value ignore-color")
    ticker_price = soup.find_all(
    'span', class_="primary")
    ticker_price = ticker_price[1].text
    gainer= premarket_gainers_ticker.text
    dyx_gainer = float(gainer[:-1])
    print("DYX: ",dyx_gainer,"%")
    return dyx_gainer, ticker_price


def get_vix_week_diff():
    url = "https://www.marketwatch.com/investing/index/vix"
    header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.3"}
    response = requests.get(url, headers=header)
    soup = BS(response.content, "html.parser")
    premarket_gainers_ticker = soup.find(
    'li', class_="content__item value ignore-color")
    gainer= premarket_gainers_ticker.text
    vix_gainer = float(gainer[:-1])
    ticker_price = soup.find_all(
    'span', class_="primary")
    ticker_price = ticker_price[1].text
    print("VIX: ",vix_gainer,"%")
    return vix_gainer, ticker_price

def get_tnx_month_diff():
    url = "https://www.marketwatch.com/investing/index/tnx?countrycode=xx"
    header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.3"}
    response = requests.get(url, headers=header)
    soup = BS(response.content, "html.parser")
    premarket_gainers_ticker = soup.find_all(
    'li', class_="content__item value ignore-color")
    gainer= premarket_gainers_ticker
    tnx_gainer = premarket_gainers_ticker[1].text
    tnx_gainer = float(tnx_gainer[:-1])
    print("TNX 1 month: ",tnx_gainer,"%")
    return tnx_gainer

def get_dyx_month_diff():
    url = "https://www.marketwatch.com/investing/index/dxy"
    header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.3"}
    response = requests.get(url, headers=header)
    soup = BS(response.content, "html.parser")
    premarket_gainers_ticker = soup.find_all(
    'li', class_="content__item value ignore-color")
    gainer= premarket_gainers_ticker
    dyx_gainer = premarket_gainers_ticker[1].text
    dyx_gainer = float(dyx_gainer[:-1])
    print("DYX 1 month: ",dyx_gainer,"%")
    return dyx_gainer

def get_vix_month_diff():
    url = "https://www.marketwatch.com/investing/index/vix"
    header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.3"}
    response = requests.get(url, headers=header)
    soup = BS(response.content, "html.parser")
    premarket_gainers_ticker = soup.find_all(
    'li', class_="content__item value ignore-color")
    gainer= premarket_gainers_ticker
    vix_gainer = premarket_gainers_ticker[1].text
    vix_gainer = float(vix_gainer[:-1])
    print("VIX 1 month: ",vix_gainer,"%")
    return vix_gainer

# soup = get_tnx_week_diff('https://www.marketwatch.com/investing/index/tnx?countrycode=xx')
get_tnx_week_diff()
# get_dyx_week_diff()
# get_vix_week_diff()
# print("\n")


# premarket_gainers_ticker = soup.find(
#     'li', class_="content__item value ignore-color")
# gainer= premarket_gainers_ticker.text

# premarket_gainers_change = soup.find_all(
#     'li', class_="content__item value ignore-color")
get_tnx_month_diff()
# get_dyx_month_diff()
# get_vix_month_diff()

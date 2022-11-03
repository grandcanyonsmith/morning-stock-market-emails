import requests
import time
year_month = time.strftime("%Y-%m-%d")
r = requests.get(
    f'https://financialmodelingprep.com/api/v4/industry_price_earning_ratio?date={year_month}&exchange=NYSE&apikey=e49e22b0865cfeea71aa0771ddf965a1'
)

print(year_month)
ratio = r.json()

# for x in ratio:
#     print(x)
year = ['2021']

for x in year:
    print(
        f'https://financialmodelingprep.com/api/v4/sector_price_earning_ratio?date={x}-{year_month}&exchange=NYSE&apikey=e49e22b0865cfeea71aa0771ddf965a1'
    )

    sectors = requests.get(
        f'https://financialmodelingprep.com/api/v4/sector_price_earning_ratio?date={x}-{year_month}&exchange=NYSE&apikey=e49e22b0865cfeea71aa0771ddf965a1'
    )

    sectors = sectors.json()

    for i in sectors:
        if i['sector'] == 'Technology':
            print(x,": ",i)

apple = []
times = []
new_group = []
stocks = ['AAPL','MA','BR','CSGP','GLOB','CDNS','PETS','NVR','TWLO','AMCX','FDX','CMG','TREX','PINS']
# stocks = ['AAPL','MA']
for stock in stocks:
    try:
        i = 0
        price = requests.get(
            f'https://financialmodelingprep.com/api/v3/historical-price-full/{stock}?from=2021-03-12&to=2021-07-09&apikey=e49e22b0865cfeea71aa0771ddf965a1'
        )

        # price = requests.get('https://financialmodelingprep.com/api/v3/historical-chart/30min/'+ stock +'?apikey=e49e22b0865cfeea71aa0771ddf965a1')
        price = price.json()
        price = price['historical']
        # print(price)
        total_len = len(price)
        for x in price:
            if x['date'] > '2021-06-18 09:30:00':
                i += 1
                # print(i," of ", total_len)
                price = x['high']
                date = x['date']
                json = {'price': price, 'date': date}
                apple.append(json)
            # if stock == 'PINS' and x['date']:
            #     print(x)



        stock_price = [x['price'] for x in apple]
        minimum = min(stock_price)
        maximum = max(stock_price)
        # print(minimum)
        # print(maximum)

        for x in apple:
            if x['price'] == minimum:
                min_value = x
                # print(min_value)
                # print(min_value['date']) 
                low = min_value['price']
        for x in apple:

            if x['price'] == maximum and min_value['date'] < x['date']:
                max_value = x
                print(max_value['date'])
                print(min_value)
                print("max",max_value)
                high = max_value['price']
                difference = float(((-(low)/high)+1)*100).__round__(2)
                print(stock,": ",difference,"%")

        print('\n')
        apple.clear()
        times.clear()
    except:
        Exception

    #     print(low_date)

    #     for x in times:
    #         stock_date = x['time']
    #         unix = requests.get('https://showcase.api.linx.twenty57.net/UnixTime/tounix?date=' + stock_date )
    #         unix = float(unix.json())
    #         if unix > float(low_date):
    #             new_group.append(x['price'])
        
    #     highest = max(new_group)
    #     for x in times:
    #         if x['price'] == highest:
    #             print(x)
    #     apple.clear()
    #     times.clear()

    #     difference = float(((-(low/highest)+1)*100).__round__(2))
    #     print(stock,": ",difference,"%")
    #     apple.clear()
    #     times.clear()
    #     print('\n')

    # print(unix.json())

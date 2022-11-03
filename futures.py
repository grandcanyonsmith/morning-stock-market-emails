import requests
import csv

r = requests.get('https://eodhistoricaldata.com/api/intraday/AAPL.US?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&interval=1m&from=1621014898&to=1624973100')
# r = requests.get('https://eodhistoricaldata.com/api/intraday/AAPL.US?api_token=60dced076a0221.83851155') 

# resp = r.json()

# print(r.text)

with open('output.csv', 'w+') as f:
    f.write(r.text)

heights = []
highest_gain = []
i = 0
ally = []
prices = []
all_gains = []
high_al = []
list_of_options = ['GOOG  191122C01110000','GOOG  191122C01090000','GOOG  191122C01242500']

with open('output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    i = 0
    empty = []
    all_id = []
    certain_option = []
    big = []
    for row in csv_reader:
        # i += 1
        try:
            price= row[6]

            price = row[5]
            # print(price)
            json = {"price":price}
            prices.append(json)
        except:
            Exception

    for x in prices:
        try:
            number = x['price']
            real_number = 0 if number == '' else float(number)
            heights.append(real_number)
        except:
            Exception
    hi = 0
    i = 0
    ally = []
    lil_high = [0]
    yup = []
    new_highest = 0

    for i in range(len(heights)):
        i += 1
        print(i)

        ally = []
        highest = []

        wee = []
        for j in range(i+1, len(heights)):
            
            # print(i)
            # print(j)
            # print(heights[i])
            wee.append(heights[i])
            # print("wut",heights[j])
            # print("YES",max(wee))
            sell_out = float(max(wee))-(float(max(wee))*.50)
            if heights[i] >= heights[j] or float(heights[i]) <= float(
                sell_out
            ):
                break


            # print("yes")

            yes = (((float(heights[j])/float(heights[i]))-1)*100).__round__(2)
            json = {"one":heights[i],"two":heights[j],"diff":yes}
            # print("YEAH",json)
            highest.append(json)
            wee.append(heights[j])
    for x in highest:
        high = x['diff']
        one = x['one']
        two = x['two']
        json = {"one":one,"two":two,"diff":high}
        # print(json)
        ally.append(json)
        # print("ally",ally)
    # prices.clear()
    # highest.clear()
    # heights.clear()


    #     print("ally",ally)
    #     for x in ally:
    #         yeah = x['diff']
    #         big.append(yeah)
    #         print(yeah)
    #     print("B IG",big)
    #     print("MAX",max(big))
    # print("big",big)
    # print("MAX",max(big))
    # print(ally)
    res = {}
    for dic in ally:
        for key, val in dic.items():
            res[key] = max(res[key], val) if key in res else val
    print(res[key])

try:
    for x in ally:
        if x['diff'] == res[key]:
            print(x)
            all_gains.append(x)
            break
except:
    Exception
    

    
#     print(len(list_of_options))
#     prices.clear()
#     ally.clear()
# print(all_gains)
# for x in all_gains:
#     best = x['diff']
#     high_al.append(best)
# print("Best of best",max(high_al))
# bestest = max(high_al)
# for x in all_gains:
#     if bestest == x['diff']:
#         print("BEST GAIN",x,"%")
    #     highest = max(prices)
    #     lowest = min(prices)
    #     print("higest",highest)
    #     print("lowest",lowest)
    #     try:
    #         gain = (((float(highest)/float(lowest))-1)*100).__round__(2)
    #         json = {"id":x,"highest_gain":gain}
    #     except:
    #         Exception
    #         json = {"id":x,"highest_gain":0}
    #     print(json)
    #     highest_gain.append(json)
    # print(highest_gain)
    # for x in hello:
    #     number = float(x)
    #     print(number)
    #     heights.append(number)
    #     hi = 0
    #     empty = []
    #     ally = []
    # for i in range(len(heights)):
    #     print(i)
    #     highest = []
    #     yup = []
    #     try:
    #         for j in range(i+1, len(heights)):
    #             print(j)
    #             if heights[i] < heights[j]:
    #                 yes = (((heights[j]/heights[i])-1)*100).__round__(2)
    #                 json = {"one":heights[i],"two":heights[j],"diff":yes}
    #                 highest.append(json)
    #         print("highest",highest)
    #     except:
    #         Exception
    #     for x in highest:
    #         high = x['diff']
    #         one = heights[i]
    #         two = heights[j]
    #         json = {"one":heights[i],"two":heights[j],"diff":high}
    #         print(json)
    #         ally.append(json)

    # res = {}
    # for dic in ally:
    #     for key, val in dic.items():
    #         if key in res:
    #             res[key] = max(res[key], val)
    #         else:
    #             res[key] = val
    # print("highest",res[key])
    # print(hello)
def get_highest_number():

    
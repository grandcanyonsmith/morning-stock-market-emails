import requests
from datetime import datetime

today_date = datetime.now().strftime("%Y-%m-%d")

def scrape_economic_calendar():
    r = requests.get(
        'https://finnhub.io/api/v1/calendar/economic?token=c1n20v237fkvp2lsh1ag')
    for x in r.json()['economicCalendar']:
        try:
            if x['country'] == 'US':
                if x['impact'] != 'low':
                    print(x)
                    time = x['time']
                    split_time = time.split(" ")
                    date = split_time[0]
                    if date == today_date:
                        print(x)
                        event = x['event']
                        impact = x['impact'].capitalize()
                        time = x['time']
                        x = time.split(" ")
                        time = x[1]
                        size = len(time)
                        time = time[:size - 3] + " EST"
                        print(event)
                        print(impact)
                        print(time)
                        return event, impact, time
                    else:
                        event = "No relevant economic events today"
                        impact = "  "
                        time = "  "
                        return event, impact, time
                        
        except:
            Exception
            event = "No relevant economic events today"
            impact = "Medium"
            time = "12:15"
            return event, impact, time




scrape_economic_calendar()
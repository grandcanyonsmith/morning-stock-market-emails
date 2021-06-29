import requests

# client_phone_contact = ['+18016237631','+18018752975','+13852673595']


def scrape_economic_calendar():
    r = requests.get(
        'https://finnhub.io/api/v1/calendar/economic?token=c1n20v237fkvp2lsh1ag')
    for x in r.json()['economicCalendar']:
        if x['country'] == 'US':
            if x['impact'] != 'low':
                event = x['event']
                impact = x['impact'].lower()
                time = x['time']
                print(event)
                print(impact)
                print(time)
                return event, impact, time


# scrape_economic_calendar()

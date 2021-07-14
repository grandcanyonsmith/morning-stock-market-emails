import time
from datetime import datetime
from pytz import timezone
import requests

def vix_metrics():
    mst = timezone('MST')
    mst_now = datetime.now(mst)
    req = requests.get('https://squeezemetrics.com/monitor/static/DIX.csv?_t=1607864614116', timeout=300, stream=True)
    content = req.content.decode('utf-8')
    number = content.split()[-1].split(',')[1]
    data = {'date': content.split()[-1].split(',')[0], 'value green': content.split()[-1].split(',')[1],
            'value blue': float(content.split()[-1].split(',')[2])*100}
    latest = str(data['value blue'])
    current_dix = float(content.split()[-1].split(',')[2])*100
    current_dix = current_dix.__round__(2)
    the_dix_before_last = float(content.split()[-2].split(',')[2])*100
    the_dix_before_last = the_dix_before_last.__round__(2)
    # gain_or_loss = str((((current_dix/the_dix_before_last)-1)*100).__round__(2))
    gain_or_loss = (current_dix - the_dix_before_last).__round__(2)
    dix_number = float(gain_or_loss)
    print(dix_number)
    if dix_number < 0:
        dix_positive_or_negative = 'negative'
    else:
        dix_positive_or_negative = 'positive'
        gain_or_loss = "+" + str(gain_or_loss)
    return current_dix, the_dix_before_last, gain_or_loss, dix_positive_or_negative


# vix_metrics()


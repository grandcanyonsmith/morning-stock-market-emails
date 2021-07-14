import quandl 
import requests
from datetime import date
import time

r = requests.get('https://www.quandl.com/api/v3/datasets/RATEINF/INFLATION_USA.json?api_key=tM7wf3BaircRXQu_GAY4')
df = r.json()

current_inflation = df['dataset']['data'][0][1]

year_month = time.strftime("%Y-%m")
print("Inflation " + year_month + ": ",current_inflation,"%")
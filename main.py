import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from ScrapeInformation.dix import vix_metrics
from ScrapeInformation.economic_calendar import scrape_economic_calendar
from ScrapeInformation.futures import (get_dow_futures, get_nasdaq_futures,
                                       get_spy_futures)
from ScrapeInformation.premarket_gainers import print_gainers
from ScrapeInformation.macro_stats import *
from styles import css
import time
import schedule

def main():
  today_date = datetime.now().strftime("%m-%d-%Y")
  # me == my email address
  # you == recipient's email address
  me = "themorningmarketnews@gmail.com"
  # you = ['themorningmarketnews@gmail.com']
  you = ['themorningmarketnews@gmail.com','canyonfsmith@gmail.com',"quaidrholder@gmail.com","benjcrowley@gmail.com "]

  bullish_img = "'https://res.cloudinary.com/apexx/image/upload/v1625592197/Screen_Shot_2021-07-06_at_11.01.18_AM-removebg-preview_1_qr4bif.png'"
  bearish_img = "'https://res.cloudinary.com/apexx/image/upload/v1625592165/Screen_Shot_2021-07-06_at_11.02.29_AM-removebg-preview_vgvtgv.png'"

  latest, the_dix_before_last, gain_or_loss, dix_positive_or_negative = vix_metrics()
  event, impact, time = scrape_economic_calendar()

  top_three_tickers, difference = print_gainers()
  premarket_gainer_one = top_three_tickers[0]
  premarket_gainer_two = top_three_tickers[1]
  premarket_gainer_three = top_three_tickers[2]

  gainer_one_change = difference[0]
  gainer_two_change = difference[1]
  gainer_three_change = difference[2]

  gainer_one_length = len(premarket_gainer_one)
  gainer_two_length = len(premarket_gainer_two)
  gainer_three_length = len(premarket_gainer_three)

  nasdaq_futures, nasdaq_negative_or_positive = get_nasdaq_futures()
  dow_futures, dow_negative_or_positive = get_dow_futures()
  spy_futures, spy_negative_or_positive = get_spy_futures()

  tnx_week_difference, tnx_price = get_tnx_week_diff()
  dyx_week_difference, dyx_price = get_dyx_week_diff()
  vix_week_difference, vix_price = get_vix_week_diff()

  tnx_month_difference = get_tnx_month_diff()
  dyx_month_difference = get_dyx_month_diff()
  vix_month_difference = get_vix_month_diff()

  if tnx_week_difference < 0:
    tnx_week_bg_color = '#50C878'
    tnx_week_positive_or_negative = ''
    tnx_week_index_sentiment_img = 'bullish'
  else:    
    tnx_week_bg_color = '#ff6347'
    tnx_week_positive_or_negative = '+'
    tnx_week_index_sentiment_img = 'bearish'

  if dyx_week_difference < 0:
    dyx_week_bg_color = '#50C878'
    dyx_week_positive_or_negative = ''
    dyx_week_index_sentiment_img = 'bullish'
  else:    
    dyx_week_bg_color = '#ff6347'
    dyx_week_positive_or_negative = '+'
    dyx_week_index_sentiment_img = 'bearish'

  if vix_week_difference < 0:
    vix_week_bg_color = '#50C878'
    vix_week_positive_or_negative = ''
    vix_week_index_sentiment_img = 'bullish'
  else:    
    vix_week_bg_color = '#ff6347'
    vix_week_positive_or_negative = '+'
    vix_week_index_sentiment_img = 'bearish'

  if tnx_month_difference < 0:
    tnx_month_bg_color = '#50C878'
    tnx_month_positive_or_negative = ''
    tnx_month_index_sentiment_img = 'bullish'
  else:    
    tnx_month_bg_color = '#ff6347'
    tnx_month_positive_or_negative = '+'
    tnx_month_index_sentiment_img = 'bearish'

  if dyx_month_difference < 0:
    dyx_month_bg_color = '#50C878'
    dyx_month_positive_or_negative = ''
    dyx_month_index_sentiment_img = 'bullish'
  else:    
    dyx_month_bg_color = '#ff6347'
    dyx_month_positive_or_negative = '+'
    dyx_month_index_sentiment_img = 'bearish'

  if vix_month_difference < 0:
    vix_month_bg_color = '#50C878'
    vix_month_positive_or_negative = ''
    vix_month_index_sentiment_img = 'bullish'
  else:    
    vix_month_bg_color = '#ff6347ed'
    vix_month_positive_or_negative = '+'
    vix_month_index_sentiment_img = 'bearish'

  for x in you:
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Morning Stock News Update"
    msg['From'] = me
    msg['To'] = x
    print(x)

    # Create the body of the message (a plain-text and an HTML version).
    text = "ADP National Employment&nbsp; &nbsp; &nbsp; &nbsp;"
    html = f"""\

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Template</title>
        {css}
      </head>
      <body>
        <div class="container">
          <h3 style="color: white; text-align: right;">{today_date}</h3>
          <img
            src="https://res.cloudinary.com/apexx/image/upload/v1625812988/bull_cu25gl.png"
            alt=""
            style ="
            display: block;
            margin-bottom: 0px;
            margin-left: auto;
            margin-right: auto;
            width: 30%;"
          />
          <img
            src="https://res.cloudinary.com/apexx/image/upload/v1625813212/Screen_Shot_2021-07-09_at_12.46.29_AM-removebg-preview_za2teb.png"
            alt=""
            style ="
            margin-top:0px;
            padding-top:0px;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;"
          />
          <div class="markets-wrapper">
            <div class="economic-event">
              <img
                src="https://demo.stripocdn.email/content/guids/9b98c89a-bb0d-4d23-87f1-466b704a2645/images/50621624753169481.png"
                alt=""
                style ="
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 50%;"
              />

              <section class="wrapper">
                <h3>{event}</h3>
                <h3 style="text-align: right;">{time}</h3>
              </section>

              <section class="wrapper">
                <h3>Economic Impact:</h3>
                <h3 style="color: {'#FFFF00' if impact == 'Medium' else ('white' if impact == 'Low' else 'red')}">{impact}</h3>
              </section>

              <span></span>
            </div>
            <div style="background-color: {'#ff6347' if dix_positive_or_negative == 'negative' else ('#50C878' if dix_positive_or_negative =='positive' else 'white')}" class="dix">
              <img
                src="https://demo.stripocdn.email/content/guids/9b98c89a-bb0d-4d23-87f1-466b704a2645/images/22131624753395729.png"
                alt=""
                style ="
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 50%;"
              />
              <section style="display: flex; justify-content: space-between;" class="wrapper">
                <h3>DIX:                            </h3>
                <h3 class="dix_space">{latest}%</h3>
              </section>

              <section style="display: flex; justify-content: space-between;" class="wrapper">
                <h3>Previous:                           </h3>
                <h3 class="dix_space_two">{the_dix_before_last}%</h3>
              </section>

              <section style="display: flex; justify-content: space-between;" class="wrapper">
                <h3>Difference:                          </h3>
                <h3 class="dix_space_three" style="color: {'red' if dix_positive_or_negative == 'negative' else ('green' if dix_positive_or_negative == 'positive' else 'white')}">{gain_or_loss}%</h3>
              </section>
            </div>
            <div class="pre-market-gainers">
              <img
                src="https://demo.stripocdn.email/content/guids/9b98c89a-bb0d-4d23-87f1-466b704a2645/images/37771624753032792.png"
                alt=""
                height="192.02px"
                style ="
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 40%;"
              />

              <section class="wrapper">
                <h3>{premarket_gainer_one}</h3>
                <h3 style="margin-left: {'8.25em' if gainer_one_length == 2 else ('7.5em' if gainer_one_length == 3 else '6.85em')};">+{gainer_one_change}</h3>
              </section>

              <section class="wrapper">
                <h3>{premarket_gainer_two}</h3>
                <h3 style="margin-left: {'9.25em' if gainer_two_length == 2 else ('7.5em' if gainer_two_length == 3 else '6.85em')};">+{gainer_two_change}</h3>
              </section>
              <section class="wrapper">
                <h3>{premarket_gainer_three}</h3>
                <h3 style="margin-left: {'8.25em' if gainer_three_length == 2 else ('7.5em' if gainer_three_length == 3 else '6.85em')};">+{gainer_three_change}</h3>
              </section>
            </div>
            <div style="background-color: {'#ff6347' if nasdaq_negative_or_positive == 'negative' else ('green' if nasdaq_negative_or_positive =='positive' else 'white')}"  class="futures">
              <img
                src="https://demo.stripocdn.email/content/guids/9b98c89a-bb0d-4d23-87f1-466b704a2645/images/6541624757824083.png"
                alt=""
                style ="
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 45%;"
              />

              <section class="wrapper">
                <h3>Nasdaq Futures:</h3>
                <h3 style="margin-left: 1.25em; color: {'red' if nasdaq_negative_or_positive == 'negative' else ('#66ff00' if nasdaq_negative_or_positive == 'positive' else 'white')}">{nasdaq_futures}</h3>
              </section>

              <section class="wrapper">
                <h3>Dow Futures:</h3>
                <h3 style="margin-left: 2.7em; color: {'red' if dow_negative_or_positive == 'negative' else ('#66ff00' if dow_negative_or_positive == 'positive' else 'white')}">{dow_futures}</h3>
              </section>

              <section class="wrapper">
                <h3>Spy Futures:</h3>
                <h3 style="margin-left: 3em; color: {'red' if spy_negative_or_positive == 'negative' else ('#66ff00' if spy_negative_or_positive == 'positive' else 'white')}">{spy_futures}</h3>
              </section>
                      </div>
              
              <div class="macro-economics">
                <div style="padding: 0px; margin: 2px; border: none; width: 75%; background-color: {tnx_week_bg_color}" >
                <img
                  src="{'https://res.cloudinary.com/apexx/image/upload/v1625592197/Screen_Shot_2021-07-06_at_11.01.18_AM-removebg-preview_1_qr4bif.png' if tnx_week_index_sentiment_img == 'bullish' else 'https://res.cloudinary.com/apexx/image/upload/v1625592165/Screen_Shot_2021-07-06_at_11.02.29_AM-removebg-preview_vgvtgv.png'}"
                  alt=""
                  style ="
                  display: block;
                  margin-left: auto;
                  margin-right: auto;
                  width: 45%;
                  height: 60px;"
                  />

                  <h3 style="margin-bottom: 0px !important; padding: 0px !important;" class="center">10-Year</h3>
                  <h3 style="margin: 0px !important; padding: 0px !important;" class="center">Treasury Bond</h3>
                  <div style="font-size: 12.5px; display: flex; border: none;">
                  <h3 style="text-align: left;" class="center" >{tnx_price}%</h3>
                  <h3>|</h3>
                  <h3 style="text-align: right;" class="center" >{tnx_week_positive_or_negative}{tnx_week_difference}%</h3>
                  </div>
                  <h3 class="center" >(TNX)</h3>
                  <h3 style="font-size: 9px; text-align: left; padding: 0; margin: 5px;">**5-day difference</h3> 
                </div>
                
                <div style="padding: 0px; margin: 2px; border: none; width: 75%; background-color: {dyx_week_bg_color}" >
                  <img
                  src="{'https://res.cloudinary.com/apexx/image/upload/v1625592197/Screen_Shot_2021-07-06_at_11.01.18_AM-removebg-preview_1_qr4bif.png' if dyx_week_index_sentiment_img == 'bullish' else 'https://res.cloudinary.com/apexx/image/upload/v1625592165/Screen_Shot_2021-07-06_at_11.02.29_AM-removebg-preview_vgvtgv.png'}"
                  alt=""
                  style ="
                  display: block;
                  margin-left: auto;
                  margin-right: auto;
                  width: 45%;
                  height: 60px;"
                  
                />
                
                  <h3 style="margin-bottom: 0px !important; padding: 0px !important;" class="center">US Dollar</h3>
                  <h3 style="margin: 0px !important; padding: 0px !important;" class="center">Index</h3>
                  <div style="font-size: 12.5px; display: flex; border: none;">
                  <h3 style="text-align: left;" class="center" >{dyx_price}</h3>
                  <h3>|</h3>
                  <h3 style="text-align: right;" class="center" >{dyx_week_positive_or_negative}{dyx_week_difference}%</h3>
                  </div>
                  <h3 class="center" >(DYX)</h3>  
                </div>

                <div style="padding: 0px; margin: 2px; border: none; width: 75%; background-color: {vix_week_bg_color}" >
                  <img
                  src="{'https://res.cloudinary.com/apexx/image/upload/v1625592197/Screen_Shot_2021-07-06_at_11.01.18_AM-removebg-preview_1_qr4bif.png' if vix_week_index_sentiment_img == 'bullish' else 'https://res.cloudinary.com/apexx/image/upload/v1625592165/Screen_Shot_2021-07-06_at_11.02.29_AM-removebg-preview_vgvtgv.png'}"
                  alt=""
                  style ="
                  display: block;
                  margin-left: auto;
                  margin-right: auto;
                  width: 45%;
                  height: 60px;"
                />

                <h3 style="margin-bottom: 0px !important; padding: 0px !important;" class="center">Market Fear</h3>
                <h3 style="margin: 0px !important; padding: 0px !important;" class="center">Gauge</h3>
                <div style="font-size: 12.5px; display: flex; border: none;">
                <h3 style="text-align: left;" class="center" >{vix_price}</h3>
                <h3>|</h3>
                <h3 style="text-align: right;" class="center" >{vix_week_positive_or_negative}{vix_week_difference}%</h3>
                </div>
                <h3 class="center" >(VIX)</h3>
              </div></div>
              
              <div class="macro-economics">
              
                <div class="hello" style="padding: 0px; margin: 2px; border: none; width: 75%; background-color: {tnx_month_bg_color}" >
                <img
                  src="{'https://res.cloudinary.com/apexx/image/upload/v1625592197/Screen_Shot_2021-07-06_at_11.01.18_AM-removebg-preview_1_qr4bif.png' if tnx_month_index_sentiment_img == 'bullish' else 'https://res.cloudinary.com/apexx/image/upload/v1625592165/Screen_Shot_2021-07-06_at_11.02.29_AM-removebg-preview_vgvtgv.png'}"
                  alt=""
                  style ="
                  display: block;
                  margin-left: auto;
                  margin-right: auto;
                  width: 45%;
                  height: 60px;"
                  />

                  <h3 style="margin-bottom: 0px !important; padding: 0px !important;" class="center">10-Year</h3>
                  <h3 style="margin: 0px !important; padding: 0px !important;" class="center">Treasury Bond</h3>
                  <div style="font-size: 12.5px; display: flex; border: none;">
                  <h3 style="text-align: left;" class="center" >{tnx_price}%</h3>
                  <h3>|</h3>
                  <h3 style="text-align: right;" class="center" >{tnx_month_positive_or_negative}{tnx_month_difference}%</h3>
                  </div>
                  <h3 class="center" >(TNX)</h3>            
                  <h3 style="font-size: 9px; text-align: left; padding: 0; margin: 5px;">**1-month difference</h3>
                </div>

                <div class="hello" style="padding: 0px; margin: 2px; border: none; width: 75%; background-color: {dyx_month_bg_color}" >
                  <img
                  src="{'https://res.cloudinary.com/apexx/image/upload/v1625592197/Screen_Shot_2021-07-06_at_11.01.18_AM-removebg-preview_1_qr4bif.png' if dyx_month_index_sentiment_img == 'bullish' else 'https://res.cloudinary.com/apexx/image/upload/v1625592165/Screen_Shot_2021-07-06_at_11.02.29_AM-removebg-preview_vgvtgv.png'}"
                  alt=""
                  style ="
                  display: block;
                  margin-left: auto;
                  margin-right: auto;
                  width: 45%;
                  height: 60px;"
                />
                
                  <h3 style="margin-bottom: 0px !important; padding: 0px !important;" class="center">US Dollar</h3>
                  <h3 style="margin: 0px !important; text-align: center; padding: 0px !important;" class="center">Index</h3>
                  <div style="font-size: 12.5px; display: flex; border: none;">
                  <h3 style="text-align: left;" class="center" >{dyx_price}</h3>
                  <h3>|</h3>
                  <h3 style="text-align: right;" class="center" >{dyx_month_positive_or_negative}{dyx_month_difference}%</h3>
                  </div>
                  <h3 class="center" >(DYX)</h3>            
                </div>

                <div class="hello" style="padding: 0px; margin: 2px; border: none ; width: 75%; background-color: {vix_month_bg_color}" >
                  <img
                  src="{'https://res.cloudinary.com/apexx/image/upload/v1625592197/Screen_Shot_2021-07-06_at_11.01.18_AM-removebg-preview_1_qr4bif.png' if vix_month_index_sentiment_img == 'bullish' else 'https://res.cloudinary.com/apexx/image/upload/v1625592165/Screen_Shot_2021-07-06_at_11.02.29_AM-removebg-preview_vgvtgv.png'}"
                  alt=""
                  style ="
                  display: block;
                  margin-left: auto;
                  margin-right: auto;
                  width: 45%;
                  height: 60px;"
                />

                <h3 style="margin-bottom: 0px !important; padding: 0px !important;" class="center">Market Fear</h3>
                <h3 style="margin: 0px !important; padding: 0px !important;" class="center">Gauge</h3>
                <div style="font-size: 12.5px; display: flex; border: none;">
                <h3 style="text-align: left;" class="center" >{vix_price}</h3>
                <h3>|</h3>
                <h3 style="text-align: right;" class="center" >{vix_month_positive_or_negative}{vix_month_difference}%</h3>
                </div>
                <h3 class="center" >(VIX)</h3></div></div></div>
          </div>
    </body>
    </html>

    """

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('themorningmarketnews@gmail.com', 'stocks123')
    mail.sendmail(me, x, msg.as_string())
    mail.quit()
    print("email sent")

schedule.every().monday.at("13:00").do(main)
schedule.every().tuesday.at("13:00").do(main)
schedule.every().wednesday.at("13:00").do(main)
schedule.every().thursday.at("13:00").do(main)
schedule.every().friday.at("13:00").do(main)

if __name__ == "__main__":
    print("Sending emails every day at 13:00 gmt")
    while True:
        schedule.run_pending()
        
        # time.sleep(60*60)
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from ScrapeInformation.dix import vix_metrics
from ScrapeInformation.economic_calendar import scrape_economic_calendar
from ScrapeInformation.futures import (get_dow_futures, get_nasdaq_futures,
                                       get_spy_futures)
from ScrapeInformation.premarket_gainers import print_gainers
from styles import css
import schedule
import time


def main():

    today_date = datetime.now().strftime("%m-%d-%Y")

    # me == my email address
    # you == recipient's email address
    me = "themorningmarketnews@gmail.com"
    you = ['themorningmarketnews@gmail.com', 'canyonfsmith@gmail.com',
           "quaidrholder@gmail.com", "benjcrowley@gmail.com "]

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

    # Create message container - the correct MIME type is multipart/alternative.
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
            src="https://demo.stripocdn.email/content/guids/9b98c89a-bb0d-4d23-87f1-466b704a2645/images/39361624758413736.png"
            alt=""
            style ="
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 80%;"
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
                <h3 style="margin-left: {'8.25em' if gainer_one_length == 2 else ('7.5em' if gainer_one_length == 3 else '8em')};">+{gainer_one_change}</h3>
              </section>

              <section class="wrapper">
                <h3>{premarket_gainer_two}</h3>
                <h3 style="margin-left: {'8.25em' if gainer_two_length == 2 else ('7.5em' if gainer_two_length == 3 else '8em')};">+{gainer_two_change}</h3>
              </section>
              <section class="wrapper">
                <h3>{premarket_gainer_three}</h3>
                <h3 style="margin-left: {'8.25em' if gainer_three_length == 2 else ('7.5em' if gainer_three_length == 3 else '8em')};">+{gainer_three_change}</h3>
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
          </div>
        </div>
      </body>
    </html>

    """

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
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
        time.sleep(1)
    # main()

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

today_date = datetime.now().strftime("%Y-%m-%d")

# me == my email address
# you == recipient's email address
me = "themorningmarketnews@gmail.com"
you = "themorningmarketnews@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Morning Stock News Update"
msg['From'] = me
msg['To'] = you

latest, the_dix_before_last, gain_or_loss = vix_metrics()
event, impact, time = scrape_economic_calendar()


top_three_tickers, difference = print_gainers()
premarket_gainer_one = top_three_tickers[0]
premarket_gainer_two = top_three_tickers[1]
premarket_gainer_three = top_three_tickers[2]

gainer_one_change = difference[0]
gainer_two_change = difference[1]
gainer_three_change = difference[2]

nasdaq_futures = get_nasdaq_futures()
dow_futures = get_dow_futures()
spy_futures = get_spy_futures()

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
      <h3 style="text-align: right; color: white">29/06/2021</h3>
      <img
        src="https://demo.stripocdn.email/content/guids/9b98c89a-bb0d-4d23-87f1-466b704a2645/images/74711624743032796.png"
        alt=""
        width="100%"
      />
      <div class="markets-wrapper">
        <div class="economic-event">
          <img
            src="https://demo.stripocdn.email/content/guids/9b98c89a-bb0d-4d23-87f1-466b704a2645/images/48591624742324469.png"
            alt=""
            width="100%"
          />
          <section class="wrapper">
            <h3>{event}</h3>
            <h3>{time}</h3>
          </section>

          <section class="wrapper">
            <h3>Economic Impact</h3>
            <h3 style="color: {'yellow' if impact == 'medium' else ('white' if impact == 'low' else 'red')}">{impact}</h3>
          </section>

          <span></span>
        </div>
        <div class="dix">
          <img
            src="https://demo.stripocdn.email/content/guids/9b98c89a-bb0d-4d23-87f1-466b704a2645/images/94711624742263644.png"
            alt=""
            width="100%"
          />
          <section class="wrapper">
            <h3>DIX</h3>
            <h3>{latest}</h3>
          </section>

          <section class="wrapper">
            <h3>Previous</h3>
            <h3>{the_dix_before_last}</h3>
          </section>

          <section class="wrapper">
            <h3>Difference</h3>
            <h3>{gain_or_loss}</h3>
          </section>
        </div>
        <div class="pre-market-gainers">
          <img
            src="https://demo.stripocdn.email/content/guids/9b98c89a-bb0d-4d23-87f1-466b704a2645/images/92271624742492567.png"
            alt=""
            height="192.02px"
            width="100%"
          />

          <section class="wrapper">
            <h3>{premarket_gainer_one}</h3>
            <h3>{gainer_one_change}</h3>
          </section>

          <section class="wrapper">
            <h3>{premarket_gainer_two}</h3>
            <h3>{gainer_two_change}</h3>
          </section>
          <section class="wrapper">
            <h3>{premarket_gainer_three}</h3>
            <h3>{gainer_three_change}</h3>
          </section>
        </div>
        <div class="futures">
          <img
            src="https://demo.stripocdn.email/content/guids/9b98c89a-bb0d-4d23-87f1-466b704a2645/images/50031624742592935.png"
            alt=""
            width="100%"
            height="192.02px"
          />
          <section class="wrapper">
            <h3>Nasdaq Futures</h3>
            <h3>{nasdaq_futures}</h3>
          </section>

          <section class="wrapper">
            <h3>Dow Futures</h3>
            <h3>{dow_futures}</h3>
          </section>

          <section class="wrapper">
            <h3>Spy Futures</h3>
            <h3>{spy_futures}</h3>
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
mail.sendmail(me, you, msg.as_string())
mail.quit()
print("email sent")

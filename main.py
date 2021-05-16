import smtplib
import datetime as dt
import random

my_email = "iamgrace2113@gmail.com" #sample
password = "<YOUR_PASSWORD>"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with open("quotes.txt") as motivation:
        quotes = motivation.readlines()
        quote_for_today = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="iamgrace2113@yahoo.com",
            msg=f"Subject:Monday's Motivation\n\n{quote_for_today}")

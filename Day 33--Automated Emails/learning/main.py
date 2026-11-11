import smtplib
import datetime as dt
import random
MY_EMAIL = "yorojeff0@gmail.com"
MY_PASSWORD = "maij oxml hgra dwmc"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()

    connection.login(MY_EMAIL, MY_PASSWORD)

    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="marknjoku34@gmail.com",
        msg="Subject:Hello\n\nThis is a test email."
    )


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("Day 33--Automated Emails/quotes.txt")as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()

        connection.login(MY_EMAIL, MY_PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Wednesday Motivation\n\n{quote}"
        )

import pandas
import smtplib
import datetime as dt
import random


MY_EMAIL = "yorojeff0@gmail.com"
MY_PASSWORD = "maij oxml hgra dwmc"


now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_day, today_month)


data = pandas.read_csv(
    "D:/Documents/100Days of Python/Day 33--Automated Emails/birthdays.csv")


birthday_dict = {(data_row["month"], data_row["day"])
                  : data_row for (index, data_row) in data.iterrows()}


if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"D:/Documents/100Days of Python/Day 33--Automated Emails/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()

        connection.login(MY_EMAIL, MY_PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )

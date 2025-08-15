import pandas
import datetime as dt
import os
import random
import smtplib


data = pandas.read_csv(
    "C:/Users/akash/OneDrive/Documents/Python/Projects/birthday_wisher/birthdays.csv"
)

birthday_dic = data.to_dict(orient="records")

now = dt.datetime.now()
today_day = now.day
today_month = now.month

username = "practiceemailpython@gmail.com"
password = "dxxttmindhargphc"

for i in birthday_dic:
    if today_month == i["month"] and today_day == i["day"]:
        # NOTE: choosing a random letter from a dictionary of letters
        random_letter = random.choice(
            os.listdir(
                "C:/Users/akash/OneDrive/Documents/Python/Projects/birthday_wisher/letter_templates/"
            )
        )
        # NOTE: openning that random letter
        with open(
            f"C:/Users/akash/OneDrive/Documents/Python/Projects/birthday_wisher/letter_templates/{random_letter}",
            "r",
        ) as letter_templates:
            letter = letter_templates.read()
            # replacing the name for whoever's birthday it is
            final_letter = letter.replace("[NAME]", i["name"])

        # NOTE: sending the mail
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=username, password=password)
            connection.sendmail(
                from_addr=username,
                to_addrs=i["email"],
                msg=f"subject: Happy Birthday!!\n\n{final_letter}",
            )

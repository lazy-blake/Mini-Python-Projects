import os
from smtplib import SMTP

from data_manager import DataManager
from dotenv import load_dotenv
from flight_data import FlightData
from twilio.rest import Client

load_dotenv()
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data = DataManager()
sheet_data = data.sheet_data
customer_emails = data.get_user_email()
flight = FlightData()
account_sid = os.getenv("ACC_ID")
auth_token = os.getenv("AUTH_TOKEN")
username = os.getenv("SMTP_USERNAME") or ""
password = os.getenv("SMTP_PASSWORD") or ""

for i in sheet_data:
    if i["iataCode"] == "":
        data.update_sheet(i)

    else:
        cheapest_flight = flight.get_price(i["iataCode"])
        if cheapest_flight and cheapest_flight[0] <= i["lowestPrice"]:
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"""Low price alert! Only E{cheapest_flight[0]} to
                     fly from {cheapest_flight[3]} to {cheapest_flight[4]}, on
                     {cheapest_flight[1]} until {cheapest_flight[2]}.""",
                from_="+15854969217",
                to="+918101569148",
            )
            print(message.status)

            for i in customer_emails:
                with SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=username, password=password)
                    connection.sendmail(
                        from_addr=username,
                        to_addrs=i,
                        msg=f"""subject: Flight Deals\n\nLow price alert! Only GBP {cheapest_flight[0]} to
                         fly from {cheapest_flight[3]} to {cheapest_flight[4]}, on
                         {cheapest_flight[1]} until {cheapest_flight[2]}.""",
                    )
        if not cheapest_flight:
            cheapest_flight = flight.get_price(i["iataCode"], is_direct=False)

            if cheapest_flight and cheapest_flight[0] <= i["lowestPrice"]:
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    body=f"""Low price alert! Only £{cheapest_flight[0]} to
                         fly from {cheapest_flight[3]} to {cheapest_flight[4]}, on
                         {cheapest_flight[1]} until {cheapest_flight[2]}. 
                         *Indirect flight*""",
                    from_="+15854969217",
                    to="+918101569148",
                )
                print(message.status)

                for i in customer_emails:
                    with SMTP("smtp.gmail.com") as connection:
                        connection.starttls()
                        connection.login(user=username, password=password)
                        connection.sendmail(
                            from_addr=username,
                            to_addrs=i,
                            msg=f"""subject: Flight Deals\n\nLow price alert! Only GBP {cheapest_flight[0]} to
                             fly from {cheapest_flight[3]} to {cheapest_flight[4]}, on
                             {cheapest_flight[1]} until {cheapest_flight[2]}.""",
                        )

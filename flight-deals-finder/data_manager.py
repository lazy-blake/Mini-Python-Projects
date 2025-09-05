import os

import requests
from dotenv import load_dotenv
from flight_search import FlightSearch

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.city_code = FlightSearch()
        self.user_endpoint = os.getenv("USER_ENDPOINT")
        self.auth = {"Authorization": f"Basic {os.getenv('AUTH')}"}
        self.response = requests.get(
            url="https://api.sheety.co/2d6b82a024bbfd9e35fde46c9fbdaa13/flightDealsFinder/prices",
            headers=self.auth,
        )
        self.get_data()

    def get_data(self):
        self.response.raise_for_status()
        self.data = self.response.json()
        self.sheet_data = self.data["prices"]

    def update_sheet(self, row) -> None:
        city_name = row["city"]
        body = {"price": {"iataCode": self.city_code.get_city(city_name)}}
        self.update = requests.put(
            url=f"https://api.sheety.co/2d6b82a024bbfd9e35fde46c9fbdaa13/flightDealsFinder/prices/{row['id']}",
            json=body,
            headers=self.auth,
        )
        self.update.raise_for_status()

    def get_user_email(self) -> list:
        response = requests.get(url=self.user_endpoint, headers=self.auth)
        response.raise_for_status()
        data = response.json()["users"]
        emails = [i["whatIsYourEmailAddress?"] for i in data]
        return emails

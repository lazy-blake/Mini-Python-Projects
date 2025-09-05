import os

import requests
from dotenv import load_dotenv

load_dotenv()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self._api_key = os.getenv("API_KEY")
        self._api_secret = os.getenv("API_SECRET")
        self.token = self.get_token()

    def get_token(self) -> str:
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }
        response = requests.post(
            url="https://test.api.amadeus.com/v1/security/oauth2/token",
            headers=header,
            data=body,
        )
        response.raise_for_status()
        print(response.text)

        return response.json()["access_token"]

    def get_city(self, city_name):
        city_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        header = {"Authorization": f"Bearer {self.token}"}

        body = {"keyword": city_name, "max": 2}
        response = requests.get(url=city_url, params=body, headers=header)
        response.raise_for_status()

        try:
            return response.json()["data"][0]["iataCode"]
        except KeyError:
            print(f"no airport code found for {city_name}")

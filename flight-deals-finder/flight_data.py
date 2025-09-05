from datetime import datetime, timedelta

import requests
from flight_search import FlightSearch

URL_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
LOCATION = "CCU"
step_days = 7


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.flight = FlightSearch()
        self.token = self.flight.get_token()

    def get_price(self, city_code, is_direct=True):
        header = {"Authorization": f"Bearer {self.token}"}

        start_date = datetime.now() + timedelta(days=1)
        end_date = start_date + timedelta(days=180)
        current_time = start_date

        cheapest_flight = None

        while current_time <= end_date:
            body = {
                "originLocationCode": LOCATION,
                "destinationLocationCode": city_code,
                "departureDate": current_time.strftime("%Y-%m-%d"),
                "adults": 1,
                "currencyCode": "GBP",
                "nonStop": "true" if is_direct else "false",
            }
            response = requests.get(
                url=URL_ENDPOINT,
                headers=header,
                params=body,
            )

            response.raise_for_status()
            try:
                data = response.json()["data"]
                if data:
                    price = float(data[0]["price"]["total"])
                    departure_date = data[0]["itineraries"][0]["segments"][0][
                        "departure"
                    ]["at"].split("T")[0]
                    arrival_date = data[0]["itineraries"][0]["segments"][-1]["arrival"][
                        "at"
                    ].split("T")[0]
                    origin = data[0]["itineraries"][0]["segments"][0]["departure"][
                        "iataCode"
                    ]
                    destination = data[0]["itineraries"][0]["segments"][-1]["arrival"][
                        "iataCode"
                    ]

                    # Compare with previous cheapest
                    if cheapest_flight is None or price < float(cheapest_flight[0]):
                        cheapest_flight = (
                            price,
                            departure_date,
                            arrival_date,
                            origin,
                            destination,
                        )

            except (IndexError, KeyError):
                pass  # No flights this date, try next date

            current_time += timedelta(days=step_days)  # Move to next date

        return cheapest_flight

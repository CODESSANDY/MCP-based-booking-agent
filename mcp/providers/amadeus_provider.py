import os
from dotenv import load_dotenv
from amadeus import Client, ResponseError

load_dotenv()
AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")

class AmadeusProvider:
    def __init__(self):
        self.amadeus = Client(
            client_id=AMADEUS_API_KEY,
            client_secret=AMADEUS_API_SECRET
        )

    def search(self, location, check_in, check_out, guests):
        """Search hotels using Amadeus API"""
        try:
            response = self.amadeus.shopping.hotel_offers.get(
                cityCode=location.upper(),
                checkInDate=check_in,
                checkOutDate=check_out,
                adults=guests
            )
            data = response.data
            listings = []
            for h in data[:5]:
                hotel = h["hotel"]
                offer = h["offers"][0]
                listings.append({
                    "platform": "Amadeus",
                    "property_name": hotel.get("name"),
                    "location": hotel["address"]["cityName"],
                    "price_per_night": offer["price"]["total"],
                    "currency": offer["price"]["currency"],
                    "rating": hotel.get("rating", "N/A"),
                    "reviews_count": hotel.get("ratingQuantity", 0),
                    "cancellation_policy": offer["policies"].get("cancellations", [{}])[0].get("description", {}).get("text", "N/A")
                    if "policies" in offer else "N/A",
                    "url": hotel.get("contact", {}).get("url", "https://amadeus.com")
                })
            return listings
        except ResponseError as e:
            print(e)
            return []

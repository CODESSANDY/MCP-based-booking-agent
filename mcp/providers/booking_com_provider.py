import os
import requests
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

class BookingComProvider:
    def search(self, location, check_in, check_out, guests):
        """Search hotels using Booking.com RapidAPI"""
        url = "https://booking-com.p.rapidapi.com/v1/hotels/search"
        params = {
            "checkout_date": check_out,
            "checkin_date": check_in,
            "adults_number": guests,
            "dest_id": "-1456928",  # Paris city ID (example)
            "dest_type": "city",
            "order_by": "price"
        }
        headers = {
            "X-RapidAPI-Key": RAPIDAPI_KEY,
            "X-RapidAPI-Host": "booking-com.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json().get("result", [])
        listings = []

        for d in data[:5]:
            listings.append({
                "platform": "Booking.com",
                "property_name": d.get("hotel_name"),
                "location": location,
                "price_per_night": d.get("price_breakdown", {}).get("gross_price"),
                "currency": d.get("currencycode"),
                "rating": d.get("review_score"),
                "reviews_count": d.get("review_nr"),
                "cancellation_policy": "Free cancellation" if d.get("is_free_cancellable") else "Non-refundable",
                "url": d.get("url", "https://booking.com")
            })
        return listings

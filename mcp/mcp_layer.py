from .providers.booking_com_provider import BookingComProvider
from .providers.amadeus_provider import AmadeusProvider

class MCPBookingLayer:
    def __init__(self):
        self.providers = [BookingComProvider(), AmadeusProvider()]

    def search_all(self, location, check_in, check_out, guests):
        results = []
        for provider in self.providers:
            try:
                results.extend(provider.search(location, check_in, check_out, guests))
            except Exception as e:
                print(f"Provider {provider.__class__.__name__} failed: {e}")
        return results

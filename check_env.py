import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

print("Checking environment variables...")
print(f"RAPIDAPI_KEY: {'✅ Set (' + os.getenv('RAPIDAPI_KEY')[:10] + '...)' if os.getenv('RAPIDAPI_KEY') else '❌ Not set'}")
print(f"AMADEUS_API_KEY: {'✅ Set (' + os.getenv('AMADEUS_API_KEY')[:10] + '...)' if os.getenv('AMADEUS_API_KEY') else '❌ Not set'}")
print(f"AMADEUS_API_SECRET: {'✅ Set (' + os.getenv('AMADEUS_API_SECRET')[:10] + '...)' if os.getenv('AMADEUS_API_SECRET') else '❌ Not set'}")
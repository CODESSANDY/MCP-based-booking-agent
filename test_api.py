import requests
import json

print("Sending request to http://localhost:8000/search")
print("Payload:", json.dumps({"query": "Find me a hotel in Paris for 2 guests"}))

try:
    response = requests.post(
        "http://localhost:8000/search",
        json={"query": "Find me a hotel in Paris for 2 guests"},
        timeout=30
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.Timeout:
    print("Request timed out!")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
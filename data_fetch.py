
import requests
import pandas as pd

API_KEY = "7a3468a2031cc036ae51d110da0041ac"  # 🔁 Replace with your AviationStack key
BASE_URL = "http://api.aviationstack.com/v1/flights"

def fetch_flight_data(limit=5):
    params = {
        'access_key': API_KEY,
        'limit': limit
    }

    print("🌐 Sending API request...")
    response = requests.get(BASE_URL, params=params)

    print("📥 Status Code:", response.status_code)
    print("🔍 Raw Response:", response.text[:500])

    if response.status_code == 200:
        try:
            data = response.json()['data']
        except KeyError:
            print("❌ 'data' key missing in response")
            return pd.DataFrame()

        flights = []

        for item in data:
            flights.append({
                'airline': item['airline']['name'],
                'flight': item['flight']['iata'],
                'departure_airport': item['departure']['airport'],
                'arrival_airport': item['arrival']['airport'],
                'departure_time': item['departure']['scheduled'],
                'arrival_time': item['arrival']['scheduled']
            })

        df = pd.DataFrame(flights)
        return df
    else:
        print("❌ Request failed with code:", response.status_code)
        return pd.DataFrame()


import requests
from datetime import datetime

print()

MY_LAT = 51.587351
MY_LONG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# print(data)
sunrise = data['results']['sunrise']
print(sunrise)
sunset = data['results']['sunset']

now = datetime.now()
print(now)

# Split to get hour time
print()
sunrise_hour = sunrise.split("T")[1].split(":")[0]
print(f"Sunrise Hour: {sunrise_hour}")
sunset_hour = sunset.split("T")[1].split(":")[0]
print(f"Sunset Hour: {sunset_hour}")

print(f"Hour Now: {now.hour}")

print()

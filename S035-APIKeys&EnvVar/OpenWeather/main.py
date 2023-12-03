import requests
import json
import smtplib

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "___INSERT YOUR API KEY HERE___"
my_lat_long = (-29.829156, 31.030319)

email = "@gmail.com"
password = "___YOUR EMAIL PASSWORD___"

parameters = {
    "lat": my_lat_long[0],
    "lon": my_lat_long[1],
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

print(parameters)

# request for data
# response = requests.get(url=OWM_Endpoint, params=parameters)
# response.raise_for_status()
# print(response.status_code)
# print(response)

# save data in a json file
# weather_data = response.json()
# print(weather_data)
# with open("weather_data.json", "w") as data_file:
#     json.dump(weather_data, data_file, indent=4)

try:
    with open("weather_data.json") as data_file:
        weather_data = json.load(data_file)
except FileNotFoundError:
    print("Need to request for data")

might_rain = False

# hourly_weather = weather_data["hourly"]
# for weather_now in hourly_weather:
#     weather_id = weather_now["weather"][0]["id"]
#     if weather_id < 800:
#         might_rain = True

# Only for 12 hours
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        might_rain = True

if might_rain:
    print("\n\nBring an Umbrella\n")
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs="@yahoo.com",
                msg="Subject: Rain!\n\nIt's gonna rain today, carry an umbrela"
            )
    except smtplib.SMTPAuthenticationError:
        print("Cannot login to email, did not send message.")

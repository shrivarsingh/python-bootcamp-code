import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

MY_EMAIL = "@gmail.com"
MY_PASSWORD = ""


# Your position is within +5 or -5 degrees of the ISS position.
def in_range(my_lat_pos, my_long_pos, iss_latitude_pos, iss_longitude_pos):
    if my_lat_pos - 5.0 <= iss_latitude_pos <= my_lat_pos + 5.0:
        if my_long_pos - 5.0 <= iss_longitude_pos <= my_long_pos + 5.0:
            return True
        else:
            return False
    else:
        return False


while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])  # Convert into float
    iss_longitude = float(data["iss_position"]["longitude"])  # Convert into float

    print(f"\n--- CHECKING ---\nISS Position: {iss_latitude}, {iss_longitude}")
    print(f"My Position: {MY_LAT}, {MY_LONG}")

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])  # Convert into int
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])  # Convert into int

    time_now = datetime.now()
    print(f"Time @ {time_now}")

    # If the ISS is close to my current position
    iss_in_range = in_range(MY_LAT, MY_LONG, iss_latitude, iss_longitude)
    print(f"In range = {iss_in_range}")

    # and it is currently dark
    if sunset <= time_now.hour <= sunrise:
        is_dark = True
    else:
        is_dark = False
    print(f"Is dark outside = {is_dark}")

    # Then send me an email to tell me to look up.
    if iss_in_range and is_dark:
        with smtplib.SMTP("smtp.google.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: ISS Notifier\n\nLook up!"
            )
            print("Email sent.")
    else:
        print("Conditions not met.\nNo Email sent.")
    # BONUS: run the code every 60 seconds.
    time.sleep(60)

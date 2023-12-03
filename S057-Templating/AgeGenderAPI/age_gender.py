import requests

AGIFY_API = "https://api.agify.io/"
GENDERIZR_API = "https://api.genderize.io/"

name = input("Hi! What is your name?\n> ")

params = {
    "name": name,
}


response = requests.get(url=AGIFY_API, params=params)
response.raise_for_status()
age_data = response.json()
response = requests.get(url=GENDERIZR_API, params=params)
response.raise_for_status()
gender_data = response.json()
 
age = age_data["age"]
gender = gender_data["gender"]

print(f"Hi {name},\nI think you are {gender},\nand maybe {age} years old.")

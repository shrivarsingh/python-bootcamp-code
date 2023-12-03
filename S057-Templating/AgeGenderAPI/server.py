from flask import Flask, render_template
import random
import datetime
import requests

AGIFY_API = "https://api.agify.io/"
GENDERIZR_API = "https://api.genderize.io/"

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(0, 100)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    params = {"name": name}
    response = requests.get(url=AGIFY_API, params=params)
    response.raise_for_status()
    age_data = response.json()
    response = requests.get(url=GENDERIZR_API, params=params)
    response.raise_for_status()
    gender_data = response.json()
    age = age_data["age"]
    gender = gender_data["gender"]

    return render_template("guess.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)

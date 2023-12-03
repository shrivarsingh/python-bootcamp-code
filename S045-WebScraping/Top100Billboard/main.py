import requests
from bs4 import BeautifulSoup

URL =  "https://www.billboard.com/charts/hot-100"

billboard_date = input("Which year do you want to travel to? Type the date in this format YYYY-DD-MM.\n> ")

response = requests.get(f"{URL}/{billboard_date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
print(f"{soup.title.text}")

songs_web_list = soup.findAll(class_="chart-element__information__song")
artists_web_list = soup.findAll(class_="chart-element__information__artist")
songs = [song_web.get_text() for song_web in songs_web_list]
artists = [artist_web.get_text() for artist_web in artists_web_list]
for song in songs:
    print(f"{songs.index(song)+1}. {song} by {artists[songs.index(song)]}")
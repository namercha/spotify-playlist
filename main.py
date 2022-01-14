import requests
from bs4 import BeautifulSoup

date = input("What year do you want to travel to? Type the date in the formal YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100/" + date + "/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_songs = soup.find_all(name="div", class_="o-chart-results-list-row-container")
songs = [song.find(name="h3", id="title-of-a-story").getText().strip() for song in all_songs]
print(songs)

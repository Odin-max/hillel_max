import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://lyrsense.com/lana_del_rey").text
soup = BeautifulSoup(html_text, "lxml")
title_element = soup.find("h1", style="padding-top:5px;")
if title_element:
    title_text = title_element.text.strip()
    author = title_text.split("песен", 1)[1].strip()
    songs = soup.find_all("strong", class_="albumTitle")

    print(f"Here is the list of songs from {author}: ")
    for song in songs:
        song_text = song.text
        print(song_text)
else:
    print("Не удалось найти информацию об исполнителе.")

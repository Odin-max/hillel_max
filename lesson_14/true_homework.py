import asyncio

import aiohttp
from bs4 import BeautifulSoup


async def get_songs_by_artist(artist_name, session):
    url = f"https://lyrsense.com/{artist_name.replace(' ', '_')}"
    async with session.get(url) as response:
        html_text = await response.text()
    soup = BeautifulSoup(html_text, "lxml")
    title_element = soup.find("h1", style="padding-top:5px;")
    if title_element:
        title_text = title_element.text.strip()
        author = title_text.split("песен", 1)[1].strip()
        songs = soup.find_all("strong", class_="albumTitle")
        result = [f"Here is the list of songs from {author}: "]
        for song in songs:
            song_text = song.text
            result.append(song_text)
        return "\n".join(result)
    else:
        return f"There is no {artist_name} on Lyrsense.com"


artist_names = ["lana_del_rey", "adele", "ed_sheeran"]
base_url = "https://lyrsense.com/"


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            get_songs_by_artist(artist_name, session)
            for artist_name in artist_names
        ]
        results = await asyncio.gather(*tasks)

        for artist_name, result in zip(artist_names, results):
            with open(f"{artist_name}.txt", "w", encoding="utf-8") as file:
                file.write(result)
                print(f"Saved in {artist_name}.txt")


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import sys

import aiohttp
import httpx

BASE_URL = "https://pokeapi.co/api/v2"


async def pokemons_requests(urls: list[str]):
    import requests

    tasks = [asyncio.to_thread(requests.get, url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results


def pokemons_grequests(urls: list[str]):
    import grequests

    results = grequests.map(grequests.get(url) for url in urls)
    return results


async def pokemons_httpx(urls: list[str]):
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for url in urls]
        results = await asyncio.gather(*tasks)
    return results


async def _pokemons_aiohttp(session, url):
    async with session.get(url) as response:
        return await response.json()


async def pokemons_aiohttp(urls: list[str]):
    async with aiohttp.ClientSession() as session:
        tasks = [_pokemons_aiohttp(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    return results


def main():
    urls = [f"{BASE_URL}/pokemon/{i}" for i in range(1, 50)]

    if len(sys.argv) != 2:
        print("Usage: python script.py [requests|grequests|httpx|aiohttp]")
        sys.exit(1)

    choice = sys.argv[1]
    if choice == "requests":
        results = asyncio.run(pokemons_requests(urls))
    elif choice == "grequests":
        results = pokemons_grequests(urls)
    elif choice == "httpx":
        results = asyncio.run(pokemons_httpx(urls))
    elif choice == "aiohttp":
        results = asyncio.run(pokemons_aiohttp(urls))
    else:
        print("Unknown choice")
        sys.exit(1)

    print(results)


if __name__ == "__main__":
    main()

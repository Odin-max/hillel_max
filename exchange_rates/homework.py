import asyncio
import sys

import aiohttp

API_KEY = "NIJYOYBK8SRHLCT1"


async def fetch_exchange_rate(session, ex_currency, target_currency):
    """Fetch the exchange rate from the specified source currency
       to the specified target currency.

    Args:
        session: An aiohttp.ClientSession object.
        ex_currency: The source currency code.
        target_currency: The target currency code.

    Returns:
        A string containing the exchange rate
    """

    url = (
        "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={ex_currency}&"
        f"to_currency={target_currency}&"
        f"apikey={API_KEY}"
    )
    try:
        async with session.get(url) as response:
            data = await response.json()
            ex_rate = data.get("Realtime Currency Exchange Rate", {}).get(
                "5. Exchange Rate"
            )
            if ex_rate:
                return f"{ex_currency} to {target_currency}. Rate: {ex_rate}"
            else:
                return f"Failed to get {ex_currency} to {target_currency} rate"
    except aiohttp.ClientError as exch:
        return f"Error fetching {ex_currency} to {target_currency} rate:{exch}"


async def main():
    if len(sys.argv) < 4:
        print(
            "Invalid request. U should use:"
            "python homework.py (currency u want exchange to)"
            "--target (target currency)"
        )
        return

    exchange_currencies = sys.argv[1:-2]
    target_currency = sys.argv[-1]

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_exchange_rate(session, ex_currency, target_currency)
            for ex_currency in exchange_currencies
        ]
        exchange_rates = await asyncio.gather(*tasks)

    for rate in exchange_rates:
        print(rate)


if __name__ == "__main__":
    asyncio.run(main())

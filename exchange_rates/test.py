from pydantic import BaseModel, Field


class MoreExchangeRateInfo(BaseModel):
    rate: float


class ExchangeRate(BaseModel):
    currency_from: str = Field(alias="Blablabla")
    currency_to: str
    more: MoreExchangeRateInfo


response = {
    "Blablabla": "usd",
    "currency_to": "uah",
    "more": {"rate": "36.5"},
}

rate = ExchangeRate(**response)
print(rate)
{
    "Realtime Currency Exchange Rate": {
        "1. From_Currency Code": "USD",
        "2. From_Currency Name": "United States " "Dollar",
        "3. To_Currency Code": "JPY",
        "4. To_Currency Name": "Japanese Yen",
        "5. Exchange Rate": "148.79300000",
        "6. Last Refreshed": "2023-10-10 15:26:01",
        "7. Time Zone": "UTC",
        "8. Bid Price": "148.78920000",
        "9. Ask Price": "148.79890000",
    }
}

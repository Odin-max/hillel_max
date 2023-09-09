exchange_value = {
    "USD": {
        "EUR": 0.93,
        "UAH": 36.92,
        "USD": 1.0,
    },  # If usd to usd no convertation happens
    "EUR": {"USD": 1.07, "UAH": 39.54},
    "UAH": {"USD": 0.027, "EUR": 0.025},
}


class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def convert_to(self, target_currency, exchange_value):
        if self.currency not in exchange_value:
            raise ValueError(
                f"Currency conversion for {self.currency} is not available"
            )

        rate_to_target_currency = 1.0

        if self.currency != target_currency:
            rate_to_target_currency *= exchange_value[self.currency].get(
                target_currency, 1.0
            )

        amount_in_target_currency = self.amount * rate_to_target_currency

        return Price(amount_in_target_currency, target_currency)

    def __add__(self, another):
        if not isinstance(another, Price):
            raise ValueError("Can only add instances of the 'Price' class")

        if self.currency == another.currency:
            return Price(self.amount + another.amount, self.currency)

        self_usd = self.convert_to("USD", exchange_value)
        another_usd = another.convert_to("USD", exchange_value)

        return self_usd + another_usd

    def __sub__(self, another):
        if not isinstance(another, Price):
            raise ValueError("Can only subtract instances of the Price class")

        if self.currency == another.currency:
            return Price(self.amount - another.amount, self.currency)

        self_usd = self.convert_to("USD", exchange_value)
        another_usd = another.convert_to("USD", exchange_value)

        return self_usd - another_usd


a = Price(amount=100, currency="USD")
b = Price(amount=1000, currency="USD")
c = a + b
print(c)
a = Price(amount=100, currency="UAH")
b = Price(amount=1000, currency="USD")
c = a + b
print(c)
a = Price(amount=100, currency="UAH")
b = Price(amount=1000, currency="EUR")
c = a + b
print(c)

from typing import Any

methods_blacklist = ["_connected_to_the_atm", "_count_the_cash", "_get_money"]


class PaymentSystem:
    def __init__(self) -> None:
        self.connected_to_the_atm: bool = False

    def __getattribute__(self, name: str) -> Any:
        print(f"Accessing to attribute: {name} ")
        if name in methods_blacklist:
            raise Exception(f"This attribute {name} is private ")
        return object.__getattribute__(self, name)
        # return super().__getattribute__(name)

    def deposit(self, amount: int):
        pass

    def _connect_to_the_atm(self):
        self.connected_to_the_atm = True
        print("Connected to the ATM")

    def _count_the_cash(self, amount):
        # if self.connected_to_the_atm is False:
        #     raise Exception("You are not connected")
        print("Counting the cash in the ATM")
        print(f"Total: {amount}")

    # def _PaymentSystem__getmoney(self):
    def _get_money(self):
        # if self.connected_to_the_atm is False:
        #     raise Exception("You are not connected")
        print("Returning money to the user")

    def withdraw(self, amount: int):
        self._connect_to_the_atm()
        self._count_the_cash(amount)
        self._get_money()


privat = PaymentSystem()

# privat.deposit(amount=100)
privat.withdraw(amount=100)
# privat._get_money()

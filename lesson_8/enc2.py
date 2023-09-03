class PaymentSystem:
    def __init__(self) -> None:
        self.connected_to_the_atm: bool = False
        self.__deposit = 0

    # getter
    @property
    def deposit(self):
        return self.__deposit

    # setter
    @deposit.setter
    def deposit(self):
        return self.__deposit

    # deleter
    @deposit.deleter
    def deposit(self):
        print("Can not delete the object")


privat = PaymentSystem()

print(privat.deposit)

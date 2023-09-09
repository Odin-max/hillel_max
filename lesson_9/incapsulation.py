from typing import Any


class User:
    def __init__(self, username: str, password: str) -> None:
        self.username: str = username
        self._password: str = password
        self._authorized = False

    def __getattribute__(self, name: str) -> Any:
        if name == "password":
            return "Access denied"
        return super().__getattribute__(name)

    def login(self, username: str, password: str):
        if self.username == username and self._password == password:
            self._authorized = True
        else:
            self._authorized = False

    @property
    def is_authorized(self):
        return self._authorized

    @property
    def password(self):
        return "*******"


john = User(username="john", password="12345")


def login(username: str, password: str):
    john.login(username, password)
    print(john.password)
    if john.is_authorized:
        print("Success")
    else:
        print("ACCESS DENIED")


login("john", "12345")

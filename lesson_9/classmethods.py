import random
import string


class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @classmethod
    def create_with_temp_password(cls, username: str):
        temp_chars: list[str] = [
            random.choice(string.ascii_letters) for _ in range(10)
        ]
        temp_password = "".join(temp_chars)

        return cls(username=temp_chars, password=temp_password)


john = User(username="john", password="12345")
john = User.create_with_temp_password(username="john")
# john = create_user_with_temp_password(username="john")

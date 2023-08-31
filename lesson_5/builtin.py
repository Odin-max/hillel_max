from itertools import zip_longest
from pprint import pprint as print


class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"{self.name}: blablabla"

    def __str__(self) -> str:
        return f"This string representation of {self.name}"


john = Person(name="John")

# print("John")
# print(repr(john))
# print(john.__str__())
# print(str(john))

john_contact_info_existence = (True, True, False, False)

# print(john_contact_info_existence)

# for item in john_contact_info_existence:
#     if item == False:
#         print("Some fields are not filled")
#         break

# if any(john_contact_info_existence):
#     print("At least one field is filled")


# team = ["Jack", "Marry", "John", "Rosa", "Mark"]

# print(ord("J"))
# print(chr(11))
# print(sorted(team))
# print(sorted(team, reverse=True))

# def by_age(item:dict):
#     return item['age']

# def ll(argument1, argument2):
#     return argument1 + argument2

# ll = lambda argument1, argument2: argument1 + argument2

team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 19, "number": 3},
    {"name": "Cavin", "age": 21, "number": 2},
]


# print(sorted(team, key= lambda item: item['age']))


class Animal:
    pass


class Dog(Animal):
    pass


spike = Dog()


john = "John"
marry = "Marry"

# print(id(team))
# print(john is marry)
# print(isinstance(spike,Animal))
# print(type(spike)==Dog)
# print(isinstance(spike,Dog))
# print(hash("name"))
# print(hash("name"))
# print(hash("name"))


def foo():
    """Some documentations"""

    pass


# print(help(foo))


names = ["John", "Marry", "Jack", "Martin"]
ages = [20, 30, 40]

# for index, name in enumerate(names):
#     print(f"{name=}, age = {ages[index]}")


for name, age in zip_longest(names, ages):
    print(f"{name=}, {age=}")

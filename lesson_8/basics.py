class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_name(self):
        print(f"The name of Person is {self.name}")

    def __str__(self):
        return f"{self.name} is {self.age}"


team = [{"name": "John", "age": 18}, {"name": "Marry", "age": 22}]

john = Person(name="John", age=12)
marry = Person(name="Marry", age=17)
# print(john.__dict__)
# john = Person()
# john.name = "John"
# john.age = 12
# marry = Person()
marry.get_name()
john.get_name()
print(john)

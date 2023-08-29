# class Person:
#     def __init__(self, name:str, age:int) -> None:
#         self.name:str = name
#         self.age: int = age
import time


class Person:
    _instance = None
    _initialized: bool = False

    def perf_counter(func):
        def inner(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            exec_time = time.perf_counter() - start
            print(f"Exec time: {func.__name__}:{exec_time}")
            return result

        return inner

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, name: str, age: int) -> None:
        if self._initialized:
            return
        self.name: str = name
        self.age: int = age
        self.is_adult: bool = False
        self._initialized = True

    # @classmethod
    @staticmethod
    @perf_counter
    def greeting(name: str):
        print(f"Hello from {name}")

    @property
    def is_adultt(self) -> bool:
        if self.age < 18:
            return False
        return True


john = Person(name="John", age=12)

marry = Person(name="Marry", age=12)

Person.greeting(john.name)
john.greeting(name=john.name)

print(john.is_adultt)
# print(john.name)
# print(marry.name)

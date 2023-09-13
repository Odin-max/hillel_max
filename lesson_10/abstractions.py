from math import pi
from typing import Protocol


class CanCalculateArea(Protocol):
    def calculate_area(self) -> float:
        ...


class Circle:
    def __init__(self, radius: int) -> None:
        self.radius: int = radius

    def calculate_area(self) -> float:
        return pi * self.radius**2


class Squere:
    def __init__(self, side: int) -> None:
        self.side: int = side

    def calculate_area(self) -> float:
        return self.side**2


class Diamond:
    def __init__(self, d1, d2) -> None:
        self.d1 = d1
        self.d2 = d2

    def calculate_area(self) -> float:
        return (self.d1 * self.d2) // 2


def validate(shape: CanCalculateArea, max_limit: float):
    if shape.calculate_area() > max_limit:
        raise ValueError("THE AREA IS TOO BIG")
    return shape


def main():
    c1 = Circle(radius=12)
    s1 = Squere(side=10)

    shape1 = validate(c1, 1222)
    shape2 = validate(s1, 1222)

    print(shape1)
    print(shape2)


def foo(a: int):
    pass


foo("Hello")

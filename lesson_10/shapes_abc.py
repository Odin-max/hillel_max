from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        """Some documentation"""

    @abstractmethod
    def correct_shape(self) -> bool:
        pass


# class Shape:
#     def calculate_area(self) -> float:
#         raise NotImplementedError

#     def is_correct(self) -> bool:
#         raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius: int = radius

    def calculate_area(self) -> float:
        return pi * self.radius**2


class Squere(Shape):
    def __init__(self, side: int) -> None:
        self.side: int = side

    def calculate_area(self) -> float:
        return self.side**2


class Diamond(Shape):
    def __init__(self, d1, d2) -> None:
        self.d1 = d1
        self.d2 = d2

    def calculate_area(self) -> float:
        return (self.d1 * self.d2) // 2


class Validator:
    def validate_shape(
        self,
        shape: Shape,
        max_limit: float,
    ):
        if shape.calculate_area() > max_limit:
            raise ValueError("The area is too big")
        print(shape.is_correct())
        return shape


def main():
    c1 = Circle(radius=12)
    s1 = Squere(side=10)

    validator = Validator()
    shape1 = validator.validate_shape(c1, 1233)
    shape2 = validator.validate_shape(s1, 1233)

    print(shape1)
    print(shape2)


main()

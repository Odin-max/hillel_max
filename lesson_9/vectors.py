class Vector:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return (
            f"Vector ({self.start[0]}, {self.start[1]}); "
            f"({self.end[0]}, {self.end[1]})"
        )

    def __add__(self, other: "Vector"):
        new_start = (
            self.start[0] + other.start[0],
            self.start[1] + other.start[1],
        )
        new_end = (self.end[0] + other.end[0], self.end[1] + other.end[1])
        return Vector(new_start, new_end)


a = Vector((0, 0), (3, 1))
b = Vector((2, 2), (3, 3))

c: Vector = a + b

print(c)

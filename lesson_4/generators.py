def foo():
    print("Hello, i'm foo")


def bar(function):
    function.__call__()


def baz():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


gen = baz()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
gen.send(int(input("Next number: ")))
print(next(gen))

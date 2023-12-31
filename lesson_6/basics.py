from typing import Any, Callable


def logger(func: Callable) -> Callable:
    print(f"Running the {func.__name__}...")

    def inner(name: str):
        results: Any = func(name)
        if results:
            print(f"Results {results}")
        else:
            print("There is no results...")

    return inner


@logger
def greeting(name: str) -> None:
    print(f"Hey {name}!")


greeting("john")
# logger(greeting)(name="Max")

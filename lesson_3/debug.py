def foo(n: int) -> None:
    print(f"{n=}")
    if n > 10:
        print("> 10")
    else:
        print("< 10")


foo(14)

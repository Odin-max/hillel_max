class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, *args, **kwargs):
        print("Exiting")

    def foo(self):
        print("I am foo")


# Useless
# with MyContext() as context:
#     context.foo()

context = MyContext()
context.foo()
# context.close() Create the new one

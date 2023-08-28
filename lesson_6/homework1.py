mport functools


# MODIFY THIS DECORATOR
def reverse_string(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result[::-1]
        else:
            return None

    return inner


"""If output is a string, reverse it. Otherwise, return None."""
# def wrapper(*args, **kwargs):
#     return func(*args, **kwargs)
#     return wrapper


# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year() -> int:
    return 1957


# TEST OUPUT
print(get_university_name(), get_university_founding_year(), sep="\n")
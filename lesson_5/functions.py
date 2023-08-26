def foo():
    return 1,2,3,4,5

a,b,c,d,e = foo()

# print(a,b,c,d,e)


contact_info = ('Oleg', 'Zhanov', 'Kyiv', '33111', '+38096571123', 'man', 40)
# name, surname, city, post_index, number, sex

name, surname,*meta, age = contact_info


# print(name,surname, age)
# print()
# print(*meta)



def create_user(**kwargs):
    print("User is created")
    print(f"The name is {name}")
    print(f"The surname is {surname}")
    print(kwargs)

create_user(
    name = "John",
    surname = "Doe",
    city = "Kyiv",
    postal_code = 31211,
    phone_number = "+3809895888",
    sex = "man",
    age = 40
)


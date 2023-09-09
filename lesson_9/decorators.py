class Shop:
    user_max_size = 300

    def register(self, username, password1, password2, email):
        pass

    def login(self, username, password):
        pass

    @classmethod
    def build_new(cls, domain: str):
        # Host the application on domain ...
        # ....
        cls.user_max_size()
        # cls = Shop
        # Shop.login()

    @staticmethod
    def get_current_users_amount():
        # SELECT COUNT(id) FROM users
        return 12

    def buy(self, product: dict):
        return print(f"U bought {product}")


zara = Shop()
bershka = Shop()
Shop.build_new("bershka.com")

zara.buy(
    {"pants L": 1222},
)

# Shop.buy(
#     zara,
#     {
#         "pants L": 1222
#     },
# )

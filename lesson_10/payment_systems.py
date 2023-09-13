from abc import ABC, abstractmethod


class User:
    def __init__(self, name: str, card_name: str, cvv: str) -> None:
        self.name = name
        self.card_name = card_name
        self.cvv = cvv


class Product:
    def __init__(
        self,
        name: str,
        price: int,
    ) -> None:
        self.name = name
        self.price = price


class PaymentSystem(ABC):
    @abstractmethod
    def checkout(self, product: Product, user: User):
        pass


class PayPal(PaymentSystem):
    def checkout(self, product: Product, user: User):
        print(
            f"Checking out with PayPal for {user.name}\n "
            f"The product {product.name}[{product.price}]"
        )


class Stripe(PaymentSystem):
    def checkout(self, product: Product, user: User):
        print(
            f"Checking out with Stripe for {user.name}\n "
            f"The product {product.name} [{product.price}]"
        )


def make_purchace(payment_system: PaymentSystem, product: Product, user: User):
    print(
        f"{user.name} making purchase - {product.name} for {product.price} $ "
    )
    payment_system.checkout(product=product, user=user)


john = User(name="John", card_name="14441213113231", cvv="243")

paypal = PayPal()
stripe = Stripe()
shoes = Product(name="Adidas", price=250)

make_purchace(user=john, payment_system=paypal, product=shoes)

make_purchace(user=john, payment_system=stripe, product=shoes)

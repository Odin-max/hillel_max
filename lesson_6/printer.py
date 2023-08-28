class Printer:
    def __init__(self, name: str, ip: str, port: int) -> None:
        self.name = name
        self.ip = ip
        self.port = port

    def __str__(self) -> str:
        return f"{self.name}@{self.ip}:{self.port}"


def open_connection(printer: Printer):
    print("Connecton with Driver...")
    print(f"Connecton with {printer}...")


def print_with_printer(printer: Printer, text: str):
    print(f"Printing with {printer}")
    print(f"'{text}'")


def close_connection(printer: Printer):
    print(f"Closing connection for {printer}")


def connect(func):
    def inner(printer: Printer, document: str):
        open_connection(printer)
        func(printer, document)
        close_connection(printer)

    return inner


@connect
def print_document(printer: Printer, document: str):
    print("Document")


hp_black = Printer(name="HP black", ip="10.10.10.10.2", port=33112)
hp_white = Printer(name="HP black", ip="10.10.10.10.15", port=33112)
hp_yellow = Printer(name="HP black", ip="10.10.10.10.32", port=33111)


print_document(hp_black, "")


# open_connection(hp_black)
# print_with_printer(hp_black,"Test text")
# close_connection(hp_black)

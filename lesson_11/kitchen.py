from dataclasses import dataclass
from enum import Enum

# from threading import Thread
from multiprocessing import Process
from time import sleep


class DishSize(Enum):
    S = "S"
    M = "M"
    L = "L"


@dataclass
class Dish:
    name: str
    size: DishSize
    ingredients: list[str]


class Kitchen:
    @staticmethod
    def heat(dish: Dish):
        print(f"\n Started hitting {dish.name}")
        sleep(3)  # IO-bound task
        print(f"The {dish} is warm")

    @staticmethod
    def cook(dish: Dish):
        print(f"\n Started hitting {dish.name}")
        _ = [i for i in range(120_000_000)]  # CPU-bound task
        print(f"The {dish.name} is ready")


pizza = Dish(
    name="Peperoni",
    size=DishSize.M,
    ingredients=["tomato", "cheese", "pwperoni", "dough"],
)

salad = Dish(
    name="Caesar",
    size=DishSize.S,
    ingredients=["tomato", "cheese", "pwperoni", "dough"],
)

dishes = [pizza, salad]

# Regular Execution
# for dish in dishes:
#     Kitchen.heat(dish)

# threads = [Thread(
#     target = Kitchen.cook,
#     args=(dish,),
# ) for dish in dishes
# ]


# # for thread in threads:
# #     thread.start()

# # for thread in threads:
# #     thread.join()

# processes
tasks = [Process(target=Kitchen.cook, args=[dish]) for dish in dishes]


for task in tasks:
    task.start()

for task in tasks:
    task.join()

print("All coocked")

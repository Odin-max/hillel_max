import logging
import os
import time


class TimerContext:
    def __init__(self, test_name, include_delay=False):
        self.include_delay = include_delay
        self.test_name = test_name

    def __enter__(self):
        self.start_of_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_of_time = time.perf_counter()
        elapsed_time = self.end_of_time - self.start_of_time
        if self.include_delay:
            logging.info(
                f"{self.test_name} including delay: {elapsed_time:4f} seconds"
            )
        else:
            logging.info(
                f"Result of {self.test_name}: {elapsed_time:.4f} seconds"
            )


# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


with TimerContext(test_name="Test 1", include_delay=True):
    time.sleep(2.0)

with TimerContext(test_name="Test 2"):
    result = sum([i**2 for i in range(10000)])


with TimerContext(test_name="Test 3"):
    with open("test.txt", "w") as file:
        file.write("Hello, world!")


os.remove("test.txt")

import requests
import os
import threading
import time

# CPU-bound task (simulated heavy computation)
def encrypt_file(path: str):
    print(f"Processing image from {path} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]

# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(f"Downloading image from {image_url} in thread {threading.current_thread().name}")
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)

try:
    start_of_time = time.perf_counter()
    encrypt_file("rockyou.txt")
    end_of_time = time.perf_counter()
    encryption_counter = end_of_time - start_of_time

    start_of_time = time.perf_counter()
    download_image("https://picsum.photos/1000/1000")
    end_of_time = time.perf_counter()
    download_counter = end_of_time - start_of_time

    total = encryption_counter + download_counter

    print(f"Time taken for encryption task: {encryption_counter:.2f} seconds")
    print(f"Time taken for I/O-bound task: {download_counter:.2f} seconds")
    print(f"Total time: {total:.2f} seconds")

except Exception as e:
    print(f"Error occurred: {e}")
import time
import requests
import os
import threading
import multiprocessing

# CPU-bound task (simulated heavy computation)
def encrypt_file(path: str):
    start_time = time.perf_counter()  # Start timing the task
    print(f"Processing image from {path} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]
    end_time = time.perf_counter()  # End timing the task
    task_time = end_time - start_time
    print(f"Time taken for encrypt_file: {task_time:.2f} seconds")

# I/O-bound task (downloading image from URL)
def download_image(image_url):
    start_time = time.perf_counter()  # Start timing the task
    print(f"Downloading image from {image_url} in thread {threading.current_thread().name}")
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    end_time = time.perf_counter()  # End timing the task
    task_time = end_time - start_time
    print(f"Time taken for download_image: {task_time:.2f} seconds")


if __name__ == "__main__":
    try:
        start_time = time.perf_counter()

        download_thread = threading.Thread(target=download_image, args=("https://picsum.photos/1000/1000",))
        download_thread.start()


        encrypt_process = multiprocessing.Process(target=encrypt_file, args=("rockyou.txt",))
        encrypt_process.start()

        download_thread.join()
        encrypt_process.join()

        end_time = time.perf_counter()
        total_time = end_time - start_time

        print(f"Total time for both tasks: {total_time:.2f} seconds")

    except Exception as e:
        print(f"Error occurred: {e}")


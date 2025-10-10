# parallel_sandwich_friend.py
import multiprocessing
import threading
import time
from examplecode import *

# -----------------------------
# Multiprocessing
# -----------------------------
def run_multiprocessing(task_size=1_000_000, num_processes=6):
    processes = []
    start_time = time.time()

    for _ in range(num_processes):
        local_results = []
        p = multiprocessing.Process(target=eg_task, args=(task_size, local_results))
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    print(f"✅ Multiprocessing finished in {end_time - start_time:.2f} seconds")

# -----------------------------
# Multithreading
# -----------------------------
def run_multithreading(task_size=1_000_000, num_threads=6):
    threads = []
    start_time = time.time()

    for _ in range(num_threads):
        local_results = []
        t = threading.Thread(target=eg_task, args=(task_size, local_results))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    print(f"✅ Multithreading finished in {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    print("Running multiprocessing version...")
    run_multiprocessing(task_size=1_000_000, num_processes=6)

    print("\nRunning multithreading version...")
    run_multithreading(task_size=1_000_000, num_threads=6)

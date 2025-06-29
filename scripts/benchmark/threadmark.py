# Replace plt.show() with plt.savefig('test/thread.png')
import threading
import random
import time
import os
import matplotlib.pyplot as plt

def sort_random_list(size):
    lst = [random.randint(0, 1000000) for _ in range(size)]
    lst.sort()

def benchmark(thread_count=1, list_size=1000000):
    threads = []
    start = time.time()
    for _ in range(thread_count):
        t = threading.Thread(target=sort_random_list, args=(list_size,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    return end - start

if __name__ == "__main__":
    print(f"CPU cores: {os.cpu_count()}")
    thread_counts = [1, 2, 4, 8, 16, 32, 64]
    times = []
    for n in thread_counts:
        t = benchmark(thread_count=n)
        print(f"Threads: {n}, Time taken: {t:.4f} seconds")
        times.append(t)

    plt.figure()
    plt.plot(thread_counts, times, marker='o')
    plt.xlabel('Number of Threads')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Thread Count vs Time Taken')
    plt.grid(True)
    plt.savefig('test/thread.png')
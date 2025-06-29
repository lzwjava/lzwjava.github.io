import multiprocessing
import random
import time
import os
import matplotlib.pyplot as plt

def sort_random_list(size):
    lst = [random.randint(0, 1000000) for _ in range(size)]
    lst.sort()

def benchmark(process_count=1, list_size=1000000):
    processes = []
    start = time.time()
    for _ in range(process_count):
        p = multiprocessing.Process(target=sort_random_list, args=(list_size,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end = time.time()
    return end - start

if __name__ == "__main__":
    print(f"CPU cores: {os.cpu_count()}")
    process_counts = [1, 2, 4, 8, 16, 32, 64]
    times = []
    for n in process_counts:
        t = benchmark(process_count=n)
        print(f"Processes: {n}, Time taken: {t:.4f} seconds")
        times.append(t)

    plt.figure()
    plt.plot(process_counts, times, marker='o')
    plt.xlabel('Number of Processes')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Process Count vs Time Taken')
    plt.grid(True)
    plt.savefig('test/process.png')

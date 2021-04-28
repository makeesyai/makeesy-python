# Program: an executable file
# Process: a program that has been loaded into memory along with all the resources it needs to operate
# Thread: Unit of execution within a process.

# Multithreading: multiple threads are spawned by a process to do different tasks, at about the same time
# 1. Each thread contains its own **register set** and **local variables** (stored in stack).
# 2. All thread of a process share **global variables (stored in heap)** and the **program code**.

# IO Bound: Web scraping, database calls, and reading and writing files to disk etc.
# CPU Bound: mathematical computations, matrix multiplications, searching, image processing,
# data preprocessing etc.

# Python Global Interpreter Lock or GIL: a lock that allows only one thread to hold the control of the
# Python interpreter
import os
import time
from multiprocessing import current_process
from threading import current_thread, Thread
from time import sleep


def io_bound(sec):
    pid = os.getpid()
    curr_thread = current_thread().name
    curr_process = current_process().name
    print(f'{pid} with thread {curr_thread}, with process: {curr_process} Started')
    sleep(sec)
    print(f'{pid} with thread {curr_thread}, with process: {curr_process} Completed')


def cpu_bound(n):
    pid = os.getpid()
    curr_thread = current_thread().name
    curr_process = current_process().name
    print(f'{pid} with thread {curr_thread}, with process: {curr_process} Started')
    while n:
        n -= 1
    print(f'{pid} with thread {curr_thread}, with process: {curr_process} Completed')


if __name__ == '__main__':
    start = time.time()
    sec = 5
    num = 200000000
    # io_bound(sec)
    # io_bound(sec)
    # t1 = Thread(target=io_bound, args=(sec,))
    # t2 = Thread(target=io_bound, args=(sec,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # cpu_bound(num)
    # cpu_bound(num)
    t1 = Thread(target=cpu_bound, args=(num,))
    t2 = Thread(target=cpu_bound, args=(num,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f'The time taken={time.time() - start}')

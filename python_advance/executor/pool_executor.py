import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import sleep


def io_bound(sec):
    sleep(sec)


def cpu_bound(n):
    while n:
        n -= 1


if __name__ == '__main__':
    sec = 5
    num = 200000000

    start = time.time()
    with ThreadPoolExecutor(max_workers=8) as executor:
        # e1 = executor.submit(io_bound, sec, )
        # e2 = executor.submit(io_bound, sec, )
        # e3 = executor.submit(io_bound, sec, )
        # e4 = executor.submit(io_bound, sec, )
        t1 = executor.submit(cpu_bound, num, )
        t2 = executor.submit(cpu_bound, num, )
        t3 = executor.submit(cpu_bound, num, )
        t4 = executor.submit(cpu_bound, num, )
        # print(e1.result())
    print(f'The time taken by thread pool={time.time() - start}')

    start = time.time()
    with ProcessPoolExecutor(max_workers=8) as executor:
        # e1 = executor.submit(io_bound, sec, )
        # e2 = executor.submit(io_bound, sec, )
        # e3 = executor.submit(io_bound, sec, )
        # e4 = executor.submit(io_bound, sec, )
        p1 = executor.submit(cpu_bound, num, )
        p2 = executor.submit(cpu_bound, num, )
        p3 = executor.submit(cpu_bound, num, )
        p4 = executor.submit(cpu_bound, num, )
        # print(e1.result())
    print(f'The time taken by process pool={time.time() - start}')

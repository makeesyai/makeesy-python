import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import sleep


def io_bound(sec):
    sleep(sec)


def cpu_bound(n):
    while n:
        n -= 1


if __name__ == '__main__':
    start = time.time()
    sec = 5
    num = 200000000
    # with ThreadPoolExecutor(max_workers=4) as executor:
        # e1 = executor.submit(io_bound, sec, )
        # e2 = executor.submit(io_bound, sec, )
        # e3 = executor.submit(io_bound, sec, )
        # e4 = executor.submit(io_bound, sec, )
        # e1 = executor.submit(cpu_bound, num, )
        # e2 = executor.submit(cpu_bound, num, )
        # e3 = executor.submit(cpu_bound, num, )
        # e4 = executor.submit(cpu_bound, num, )
        # print(e1.result())

    with ProcessPoolExecutor(max_workers=4) as executor:
        # e1 = executor.submit(io_bound, sec, )
        # e2 = executor.submit(io_bound, sec, )
        # e3 = executor.submit(io_bound, sec, )
        # e4 = executor.submit(io_bound, sec, )
        e1 = executor.submit(cpu_bound, num, )
        e2 = executor.submit(cpu_bound, num, )
        e3 = executor.submit(cpu_bound, num, )
        e4 = executor.submit(cpu_bound, num, )
        # print(e1.result())
    print(f'The time taken={time.time() - start}')

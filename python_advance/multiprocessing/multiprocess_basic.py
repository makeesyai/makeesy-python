# Multiprocessing: ability of a system to support more than one processor at the same time.
# Requires-
# 1. Multiprocessor - more than one central processor.
# 2. Hyper-Threading - makes each core look like two CPUs to the operating system

import time
from multiprocessing import Process


def cpu_bound(n, name):
    print(f'Process:{name} started...')
    while n:
        n -= 1
    print(f'Process:{name} Completed!')


if __name__ == '__main__':
    start = time.time()

    n = 100000000
    # cpu_bound(n, 'Call-1')
    # cpu_bound(n, 'Call-2')
    # cpu_bound(n, 'Call-3')
    # cpu_bound(n, 'Call-4')

    p1 = Process(target=cpu_bound, args=(n, "p1", ))
    p2 = Process(target=cpu_bound, args=(n, "p2", ))
    p3 = Process(target=cpu_bound, args=(n, "p3", ))
    p4 = Process(target=cpu_bound, args=(n, "p4", ))
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    print('Joining the master...')

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("Control is back in the master program...")

    p1.close()
    p2.close()
    p3.close()
    p4.close()
    print('process closed...')

    print(f'The program took: {time.time() - start}')



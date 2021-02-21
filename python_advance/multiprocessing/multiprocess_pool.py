import multiprocessing
import os
from multiprocessing import Pool
from time import sleep

results = []


def worker(identifier):
    print(f"The process id is:{identifier}")
    sleep(5)
    return identifier


def my_callback(identifier):
    print("Callback called...")
    results.append(identifier)


if __name__ == '__main__':
    inputs = []
    num_inp = 16
    for i in range(num_inp):
        inputs.append(f'p{i}')

    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    n_process = os.cpu_count()

    # with Pool(processes=n_process) as pool:
    #     r = pool.map(func=worker, iterable=inputs)
    #     print(r)
    #     pool.close()
    #     pool.join()
    #     print("Control back to the main block...")

    # with Pool(processes=n_process) as pool:
    #     for r in pool.imap(func=worker, iterable=inputs):
    #         print(r)
    #     pool.close()
    #     pool.join()
    #     print("Control back to the main block...")

    with Pool(processes=n_process) as pool:
        for r in pool.imap_unordered(func=worker, iterable=inputs):
            print(r)
        pool.close()
        pool.join()
        print("Control back to the main block...")

    # No use of apply in parallel processing
    # with Pool(processes=n_process) as pool:
    #     results = [pool.apply(func=worker, args=(x,)) for x in inputs]
    #     print(results)
    #     pool.close()
    #     # pool.join()
    #     print("Control back to the main block...")

    # map_async without callback
    # with Pool(processes=2) as pool:
    #     r = pool.map_async(func=worker, iterable=inputs, chunksize=3)
    #     print(r.get())
    #     pool.close()
    #     pool.join()
    #     print("Control back to the main block...")

    # map_async with callback
    # with Pool(processes=2) as pool:
    #     pool.map_async(func=worker, iterable=inputs, chunksize=3, callback=my_callback)
    #     pool.close()
    #     pool.join()
    #     print("Control back to the main block...")
    #     print(results)

    # with Pool(processes=2) as pool:
    #     for x in inputs:
    #         pool.apply_async(func=worker, args=(x,), callback=my_callback)
    #     pool.close()
    #     pool.join()
    #     print("Control back to the main block...")
    #     print(results)

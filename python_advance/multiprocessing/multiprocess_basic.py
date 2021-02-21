from multiprocessing import Process
from time import sleep


def worker(identifier):
    print(f"The process for:{identifier}")
    sleep(5)


if __name__ == '__main__':

    p1 = Process(target=worker, args=("p1", ))
    p2 = Process(target=worker, args=("p2", ))
    p3 = Process(target=worker, args=("p3", ))
    p4 = Process(target=worker, args=("p4", ))

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


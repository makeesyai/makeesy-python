# Synchronization: Concurrent threads do not simultaneously
# execute the ""critical section"".

# Critical section: parts of the program where the shared resource is accessed.
from threading import Thread, Lock

num = 0


def increment():
    global num
    num += 1


def thread_task(lock):
    lock.acquire()
    for _ in range(1000000):
        increment()
    lock.release()


def main_task():
    global num
    num = 0
    lock = Lock()
    t1 = Thread(target=thread_task, name='T1', args=(lock, ))
    t2 = Thread(target=thread_task, name='T2', args=(lock, ))

    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    for i in range(10):
        main_task()
        print(f'Iteration:{i}, num={num}')

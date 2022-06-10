import threading
import time

a = 5
b = 6

a_lock = threading.Lock()
b_lock = threading.Lock()


def thread_1_calc():
    global a, b

    print('thread 1 acquiring lock a')
    a_lock.acquire(timeout=1)
    time.sleep(2)

    print('thread 1 acquiring lock b')
    b_lock.acquire(timeout=1)
    time.sleep(3)

    a += 5
    b += 6

    print("thread 2 releasing both locks")
    a_lock.release()
    b_lock.release()


def thread_2_calc():
    global a, b

    print('thread 2 acquiring lock a')
    b_lock.acquire(timeout=2)
    time.sleep(2)

    print('thread 2 acquiring lock b')
    a_lock.acquire(timeout=2)
    time.sleep(3)

    a += 5
    b += 6

    print("thread 2 releasing both locks")
    b_lock.release()
    a_lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=thread_1_calc)
    t1.start()

    t2 = threading.Thread(target=thread_2_calc)
    t2.start()

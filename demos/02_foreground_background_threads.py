import threading
import time

from multithreading.count_triplets_sum import read_numbers, count_triplets_sum

if __name__ == '__main__':
    print("started main")

    ints = read_numbers(r'..\data\1Kints.txt')
    t1 = threading.Thread(target=count_triplets_sum, daemon=True, kwargs=dict(ints=ints))
    t1.start()

    print(input("How are you, dude? "))
    time.sleep(3)
    t1.join()

    print("What are we waiting for?")
    print("ended main")

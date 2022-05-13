import threading

from multithreading.count_triplets_sum import read_numbers, count_triplets_sum
from multithreading.decorators import measure_time


@measure_time
def run_parallel():
    t1 = threading.Thread(target=count_triplets_sum, daemon=True, args=(ints_1k, 'thread for 1k nums'))
    t2 = threading.Thread(target=count_triplets_sum, daemon=True, args=(ints_2k, 'thread for 2k nums'))

    t1.start()
    t2.start()

    print('\nGoing to wait for threads')

    t1.join()
    t2.join()

@measure_time
def run_sequential(ints):
    count_triplets_sum(ints, 'main thread')


if __name__ == '__main__':
    print("started main")

    ints_1k = read_numbers(r'..\data\1Kints.txt')
    ints_2k = read_numbers(r'..\data\2Kints.txt')

    run_parallel()
    run_sequential(ints_1k)
    run_sequential(ints_2k)

    print("ended main")
    
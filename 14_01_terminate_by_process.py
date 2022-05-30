import multiprocessing
import time

from multithreading.count_triplets_sum import read_numbers

if __name__ == '__main__':
    print('started main')

    ints = read_numbers(r'data\1Kints.txt')

    p = multiprocessing.Process(target=count_triplets_sum, args=(ints,))
    p.start()

    time.sleep(5)

    p.terminate()

    print('ended main')

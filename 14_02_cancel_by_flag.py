import threading
import time

from multithreading.count_triplets_sum import read_numbers

should_stop = False


def count_triplets_sum(ints, thread_name='t'):
    print(f"started counting triplets sum in {thread_name}", end='\n')

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if should_stop:
                    print("Task was cancelled")
                    counter = -1
                    return

                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f"Triple found in {thread_name}: {ints[i]}, {ints[j]}, {ints[k]}", end='\n')

    print(f"ended count triplet sum. Triplet counter = {counter}")


if __name__ == '__main__':
    print('started main')

    ints = read_numbers(r'data\1Kints.txt')

    p = threading.Thread(target=count_triplets_sum, args=(ints,))
    p.start()

    time.sleep(5)

    should_stop = True

    time.sleep(2)

    print('ended main')
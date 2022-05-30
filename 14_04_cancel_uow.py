import threading
import time

from multithreading.count_triplets_sum import read_numbers


class ThreeSumUnitOfWork(threading.Thread):
    def __init__(self, ints, name='TestThread'):
        super().__init__(name=name)
        self.ints = ints
        self.cancel_event = threading.Event()

    def run(self):
        print(f'thread starts')
        self.count_triplets_sum(self.ints)
        print(f'thread ends')

    def cancel(self):
        self.cancel_event.set()

    def count_triplets_sum(self, ints):
        print(f"started counting triplets sum")

        n = len(ints)
        counter = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.cancel_event.is_set():
                        print("Task was cancelled")
                        counter = -1
                        return counter

                    if ints[i] + ints[j] + ints[k] == 0:
                        counter += 1
                        print(f"Triple found: {ints[i]}, {ints[j]}, {ints[k]}", end='\n')

        print(f"ended count triplet sum. Triplet counter = {counter}")
        return counter


if __name__ == '__main__':
    print('started main')

    ints = read_numbers(r'data\1Kints.txt')

    task = ThreeSumUnitOfWork(ints)
    task.start()

    time.sleep(5)

    task.cancel()
    task.join()

    print('ended main')


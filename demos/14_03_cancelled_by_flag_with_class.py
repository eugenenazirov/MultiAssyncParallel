import threading
import time

from multithreading.count_triplets_sum import read_numbers


class ThreeSumTask:
    def __init__(self, ints):
        self.ints = ints
        self.cancelled = False
        self.lock_obj = threading.Lock()

    def run(self):
        self.count_triplets_sum(self.ints)

    def cancel(self):
        with self.lock_obj:
            self.cancelled = True

    def count_triplets_sum(self, ints):
        print(f"started counting triplets sum")

        n = len(ints)
        counter = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.cancelled:
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

    ints = read_numbers(r'../data/1Kints.txt')

    task = ThreeSumTask(ints)

    t = threading.Thread(target=task.run)
    t.start()

    time.sleep(5)

    task.cancel()
    t.join()

    print('ended main')

        
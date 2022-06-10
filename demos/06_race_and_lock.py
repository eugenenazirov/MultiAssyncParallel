import concurrent.futures
import threading
import time


class BankAccount:
    def __init__(self):
        self.balance = 100 # shared data/resource
        self.lock_obj = threading.Lock()

    def update(self, transaction, amount):
        print(f"{transaction} started")

        with self.lock_obj:
            tmp_amount = self.balance
            tmp_amount += amount
            time.sleep(1)
            self.balance = tmp_amount

        print(f"{transaction} ended")


if __name__ == '__main__':

    # lock_obj = threading.Lock() #примитивы синхронизации лежат в treading
    # print(lock_obj.locked())
    #
    # lock_obj.acquire()
    # print(lock_obj.locked())
    #
    # lock_obj.release()
    # print(lock_obj.locked())


    acc = BankAccount()
    print(f"main started. acc balance = {acc.balance}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(acc.update, ('refill', 'withdraw'), (100, -200))

    print(f"end of main. acc balance = {acc.balance}")

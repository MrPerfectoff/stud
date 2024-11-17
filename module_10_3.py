import random
import threading
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for money in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for money in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()
            time.sleep(0.001)

bank = Bank()

deposit_thread = threading.Thread(target=bank.deposit)
take_thread = threading.Thread(target=bank.take)

deposit_thread.start()
take_thread.start()

deposit_thread.join()
take_thread.join()

print(f"Итоговый баланс: {bank.balance}")
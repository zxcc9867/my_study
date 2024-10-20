"""
예금 계좌, 입출금 계좌를 바탕으로 추상화된 계좌 
"""

import random
from abc import ABC, abstractmethod


class BankAccount:
    def __init__(self, owner_name, balance):
        self._account_number = random.randint(10000000, 99999999)
        self._owner_name = owner_name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self._account_number

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            return self.__balance  # 잔액반환
        else:
            raise ValueError("잔액이 없습니다.")

    @abstractmethod
    def info(self):
        pass


class SavingAccount(BankAccount):
    def __init__(self, owner_name, balance, interest_rate):
        super().__init__(owner_name, balance)
        self.__interest_rate = interest_rate
        self.__is_locked = True

    def withdraw(self, amount):
        if self.__is_locked:
            raise AttributeError("출금 제한이 걸려있습니다.")
        else:
            return super().withdraw(amount)

    def unlock(self):
        self.__is_locked = False
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)

    def get_interest_rate(self):
        return self.__interest_rate

    def info(self):
        print(
            f"""예금/{self.get_account_number()} / 잔액 {self.get_balance()}
        이율 {self.__interest_rate}%, 출금 제한 여부 : {self.__is_locked}
            """
        )

class ChekingAccount(BankAccount):
    def __init__(self, owner_name, balance, withdraw_limit=500):
        super().__init__(owner_name, balance)
        self.__withdraw_limit = withdraw_limit

    def update(self,new_limit):
        self.__withdraw_limit = new_limit

    def withdraw(self, amount):
        if self.__withdraw_limit < amount:
            raise ValueError("출금할 수 있는 금액을 초과하였습니다.")
        else :
            super().withdraw(amount)

    def info(self):
        print(
            f"""예금/{self.get_account_number()} / 잔액 {self.get_balance()}, 출금 한도 : {self.__withdraw_limit}
            """
        )

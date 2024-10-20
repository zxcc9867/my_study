"""

계좌들의 부모 클래스 

"""

from abc import ABC, abstractmethod
import secrets


class BankAccount:

    def _generate_account_number(self):
        account_number = "".join(secrets.choice("0123456789") for i in range(8))
        print(f"계좌 번호는 : {account_number} 입니다.")
        return account_number

    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
        self._account_number = self._generate_account_number()
        self._account_list = []
        self._account_list.append(self._account_number)
        print(
            f"""계좌가 만들어졌습니다. {self.name}님의 {self._account_number}이며,
              현재 당신의 잔액은 {self._balance}"""
        )

    @abstractmethod
    def info():
        pass

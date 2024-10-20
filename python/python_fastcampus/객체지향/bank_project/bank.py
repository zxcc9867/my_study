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
        self.__balance = balance
        self.__account_number = self._generate_account_number()
        self.__account_list = []
        self.__account_list.append(self.__account_number)
        print(
            f"""예금 계좌가 만들어졌습니다. {self.name}님의 {self.__account_number}이며,
              현재 당신의 잔액은 {self.__balance}이며, 현재 {"출금할 수 없습니다." if self.get_account_restriction() == True else "현재 출금할 수 있습니다."}"""
            if self.__class__.__name__ == "Saving_account"
            else f"""출금 계좌가 만들어졌습니다. {self.name}님의 계좌 번호는 {self.__account_number}이며,
                현재 당신의 잔액은 {self.__balance}원입니다.
              """
        )
    def get_account_number(self):
        return self.__account_number

    @abstractmethod
    def info():
        pass

"""

예금 계좌 

"""

from bank import BankAccount


class Saving_account(BankAccount):

    def __init__(
        self,
        owner_name,
        balance=0,
    ):
        self.__account_restriction = True
        super().__init__(owner_name, balance)

    def withdraw_money(self, name, account_number, amount):
        if account_number == self.get_account_number():
            if self.__account_restriction == True:
                raise AttributeError("이 계좌는 출금이 제한되어 있습니다.")
            else:
                print("출금을 시작합니다.")
                if self.balance > 0:
                    self.balance -= amount
                    print(
                        f"돈이 {amount}출력되었습니다. {self.name}님의 남은 잔고는 {self.balance}입니다."
                    )
                else:
                    raise ValueError("계좌의 잔고가 부족합니다.")
        else:
            raise ValueError("계좌 번호가 일치하지 않습니다. 다시 확인해주세요.")

    def get_account_restriction(self):
        return self.__account_restriction

    def unlock_account(
        self,
        name,
        account_number,
    ):
        if account_number == self.get_account_number():
            if name == self.name:
                self.__account_restriction = False
                print("출금 제한이 해제되었습니다.")
            else:
                raise ValueError(
                    "계좌의 소유자명이 일치하지 않습니다. 다시 확인해주세요."
                )
        else:
            raise ValueError("계좌 번호가 일치하지 않습니다. 다시 확인해주세요.")

    def info(self, name):
        print(
            f"""{self.name}님의 계좌 잔고는 {self.__money}이며,이자율은 {0.05}이며
              출금제한 여부는 {
                  "제한되어 있습니다." if self.__account_restriction == True else "출금할 수 있습니다." } """
        )

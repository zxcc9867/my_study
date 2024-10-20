"""

은행 고객 

"""


class Customer:

    def __init__(self, name):

        print(f"안녕하세요. {self.name}님 ! ")

    def add_withdraw_balance(self, account_number, balance, command):
        if account_number in self.__account_list and command == "add":
            self.balance += balance
        elif account_number in self.__account_list and command == "withdraw":
            self.balance -= balance

    def info(self):
        print(
            f"""{self.name}님의 계좌 리스트는 {self.__account_list}이며,
              총 보유 금액은{self.balance}입니다."""
        )  # 나중에 계산식 수정

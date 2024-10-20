from bank import BankAccount
from savings_account import Saving_account

dave = Saving_account("dave", 500)

# print(f"출금 제한 여부 {dave.get_account_restriction()}")

# dave.withdraw_money("dave", dave.get_account_number(), 300)

try:
    # 출금을 시도
    dave.withdraw_money("dave", dave.get_account_number(), 300)
except AttributeError as e:
    # 예외 메시지 출력
    print(e)

# finally:
#     # 출금 제한을 해제하는 코드
dave.unlock_account("dave", dave.get_account_number())

    # 출금 제한 여부 출력
print(f"출금 제한 여부: {dave.get_account_restriction()}")

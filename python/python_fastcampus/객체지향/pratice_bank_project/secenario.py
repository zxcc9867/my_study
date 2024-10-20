from account import SavingAccount, ChekingAccount
from user import BankUser

user1 = BankUser("Ami", 1000)
# 200달러 입출금 계좌에


user1.deduct_money(200)
account1 = ChekingAccount(user1.get_name(), 200)

user1.add_account(account1)

# 800달러를 예금 계좌에

user1.deduct_money(800)
account2 = SavingAccount(user1.get_name(), 800, 0.05)
user1.add_account(account2)

# 예금 계좌 출금 가능
account2.unlock()
# 예금 계좌에서 400 달러를 출금한 다음, 사용자에게 지급
account2.withdraw(400)
user1.add_money(400)
# 400 달러를 차감하여, 입출금 계좌로 입금한다.
user1.deduct_money(400)
account1.deposit(400)

# 보유 현금 및 계좌목록을 출력한다.
user1.get_assets()

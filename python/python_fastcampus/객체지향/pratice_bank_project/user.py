class BankUser:
    def __init__(self,owner_name,money):
        self.__accounts = []
        self.__owner_name = owner_name
        self.__money = money

    def get_name(self):
        return self.__owner_name

    def add_account(self, account):
        self.__accounts.append(account)
    def get_accounts(self):
        for account in self.__accounts:
            account.info()

    def add_money(self,amount):
        self.__money += amount

    def deduct_money(self,amount):
        self.__money -= amount

    def get_assets(self):
        print(
            f"이름 : {self.get_name()} , 보유 현금 : {self.__money}, 보유 계좌 : {self.get_accounts()}"
        )

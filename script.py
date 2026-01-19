class Account:
    """银行账户类"""

    def __init__(self, account_number, balance=0.0):
        """
        初始化账户
        :param account_number: 账号
        :param balance: 余额，默认为0
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        存款操作
        :param amount: 存款金额
        """
        if amount > 0:
            self.balance += amount
            print(f"账户 {self.account_number} 存款 {amount} 元成功，当前余额: {self.balance} 元")
        else:
            print("存款金额必须大于0")

    def withdraw(self, amount):
        """
        取款操作
        :param amount: 取款金额
        """
        if amount <= 0:
            print("取款金额必须大于0")
        elif amount > self.balance:
            print(f"账户 {self.account_number} 余额不足，当前余额: {self.balance} 元")
        else:
            self.balance -= amount
            print(f"账户 {self.account_number} 取款 {amount} 元成功，当前余额: {self.balance} 元")

    def get_balance(self):
        """
        查询余额
        :return: 当前余额
        """
        return self.balance


class Bank:
    """银行管理类"""

    def __init__(self):
        """初始化银行，创建空的账户字典"""
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0.0):
        """
        创建新账户
        :param account_number: 账号
        :param initial_balance: 初始余额
        :return: 创建的账户对象
        """
        if account_number in self.accounts:
            print(f"账号 {account_number} 已存在")
            return None

        new_account = Account(account_number, initial_balance)
        self.accounts[account_number] = new_account
        print(f"账户 {account_number} 创建成功，初始余额: {initial_balance} 元")
        return new_account

    def get_account(self, account_number):
        """
        查询账户
        :param account_number: 账号
        :return: 账户对象，如果不存在返回None
        """
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print(f"账户 {account_number} 不存在")
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        """
        账户间转账
        :param from_account_number: 转出账户
        :param to_account_number: 转入账户
        :param amount: 转账金额
        """
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if from_account and to_account:
            if amount <= 0:
                print("转账金额必须大于0")
            elif from_account.balance < amount:
                print(f"转出账户 {from_account_number} 余额不足")
            else:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"转账成功：{from_account_number} → {to_account_number}，金额: {amount} 元")


# 使用示例
if __name__ == "__main__":
    # 创建银行实例
    bank = Bank()

    # 创建账户
    account1 = bank.create_account("123456", 1000)
    account2 = bank.create_account("789012", 500)

    # 存款操作
    account1.deposit(500)

    # 取款操作
    account1.withdraw(200)

    # 查询余额
    print(f"账户1余额: {account1.get_balance()} 元")

    # 账户间转账
    bank.transfer("123456", "789012", 300)


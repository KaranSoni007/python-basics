from abc import ABC, abstractmethod

class BankAccount(ABC):
    total_account = 0

    def __init__(self, name, account_no, balance):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.name = name
        self.account_no = account_no
        self.__balance = balance

        BankAccount.total_account += 1

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.__balance

    def _update_balance(self, value):
        self.__balance = value

    def __str__(self):
        return (
            f"Account: {self.account_no} | "
            f"Name: {self.name} | "
            f"Balance: ₹{self.__balance}"
        )


class SavingAccount(BankAccount):
    min_balance = 500

    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be greater than zero"

        self._update_balance(self.get_balance() + amount)
        return f"Deposit successful. Balance = ₹{self.get_balance()}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be greater than zero"

        balance = self.get_balance()

        if balance - amount >= self.min_balance:
            self._update_balance(balance - amount)
            return f"Withdrawal successful. Balance = ₹{self.get_balance()}"

        return "Withdrawal failed. Minimum balance must be ₹500"


class CurrentAccount(BankAccount):
    overdraft_limit = 1000

    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be greater than zero"

        self._update_balance(self.get_balance() + amount)
        return f"Deposit successful. Balance = ₹{self.get_balance()}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be greater than zero"

        balance = self.get_balance()

        if balance - amount >= -self.overdraft_limit:
            self._update_balance(balance - amount)
            return f"Withdrawal successful. Balance = ₹{self.get_balance()}"

        return "Withdrawal failed. Overdraft limit exceeded"


# Create accounts
saving = SavingAccount("Rahul", 101, 5000)
current = CurrentAccount("Priya", 102, 1000)

print("=== Savings Account ===")
print(saving)
print(saving.withdraw(1000))
print(saving.deposit(500))

print("\n=== Current Account ===")
print(current)
print(current.withdraw(1500))
print(current.deposit(200))

print("\nTotal accounts:", BankAccount.total_account)

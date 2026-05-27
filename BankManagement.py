# from abc import ABC, abstractmethod
# class BankAccount(ABC):

#     total_account = 0

#     def __init__(self, name, account_no, balance):
#         self.name = name
#         self.account_no = account_no
#         self.__balance = balance #Encapsulation

#         BankAccount.total_account += 1

#         @abstractmethod

#         def deposit(self, amount):
#             pass

#         @abstractmethod

#         def withdrawn(self, amount):
#             pass

#         def getBalance(self):
#             return self.__balance
        
#         def setBalance(self, value):
#             self.__balance = value
#             return self.__balance
        
#         def __str__(self):
#             return f"Account Info : {self.account_no}"

# class SavingAccount(BankAccount):    #Inheritance

#     min_balance = 500

#     def withdrawn(self, amount):

#         isValid = self.getBalance()
#         amount >= self.min_balance

#         if(isValid):

#         else:


#     def deposit(self, amount):

#         new_amount = self.getBalance() + amount
#         self.setBalance(new_amount)
#         return f"Deposit Successful. Balance updated{self.getBalance()}"


# class CurrentAccount(BankAccount):
#     overdraft_limit = 1000

#     def withdrawn(self, amount):

#     def deposit(self, amount):



from abc import ABC, abstractmethod

class BankAccount(ABC):

    total_account = 0

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.__balance = balance   # Encapsulation

        BankAccount.total_account += 1


    @abstractmethod
    def deposit(self, amount):
        pass


    @abstractmethod
    def withdrawn(self, amount):
        pass


    def getBalance(self):
        return self.__balance


    def setBalance(self, value):
        self.__balance = value


    def __str__(self):
        return f"Account Info : {self.account_no} | Name : {self.name} | Balance : {self.__balance}"


# Saving Account
class SavingAccount(BankAccount):

    min_balance = 500

    def withdrawn(self, amount):

        balance = self.getBalance()

        if balance - amount >= self.min_balance:

            new_balance = balance - amount
            self.setBalance(new_balance)

            return f"Withdraw Successful. Balance = {self.getBalance()}"

        else:
            return "Withdraw Failed. Minimum balance must be 500"


    def deposit(self, amount):

        new_balance = self.getBalance() + amount
        self.setBalance(new_balance)

        return f"Deposit Successful. Balance = {self.getBalance()}"


# Current Account
class CurrentAccount(BankAccount):

    overdraft_limit = 1000

    def withdrawn(self, amount):

        balance = self.getBalance()

        if balance - amount >= -self.overdraft_limit:

            new_balance = balance - amount
            self.setBalance(new_balance)

            return f"Withdraw Successful. Balance = {self.getBalance()}"

        else:
            return "Withdraw Failed. Overdraft limit exceeded"


    def deposit(self, amount):

        new_balance = self.getBalance() + amount
        self.setBalance(new_balance)

        return f"Deposit Successful. Balance = {self.getBalance()}"

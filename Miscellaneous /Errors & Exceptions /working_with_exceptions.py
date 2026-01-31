'''
Working With Exceptions

What happens when your code runs into an exception during execution?  

The application/program crashes.  

End-User Applications

When you develop applications that are directly used by end-users, you need to handle different possible exceptions in your code so that the application will not crash.  

Reusable Modules

When you develop modules that are used by other developers, you should raise exceptions for different scenarios so that other developers can handle them.  

Money Transfer App Scenario
'''
#CODE
class BankAccount:
    def __init__(self, account_number):
        self.account_number = str(account_number)
        self.balance = 0

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")

    def deposit(self, amount):
        self.balance += amount


def transfer_amount(acc_1, acc_2, amount):
    acc_1.withdraw(amount)
    acc_2.deposit(amount)


user_1 = BankAccount("001")
user_2 = BankAccount("002")
user_1.deposit(250)
user_2.deposit(100)

print("User 1 Balance: {}/-".format(user_1.get_balance()))
print("User 2 Balance: {}/-".format(user_2.get_balance()))
transfer_amount(user_1, user_2, 50)
print("Transferring 50/- from User 1 to User 2")
print("User 1 Balance: {}/-".format(user_1.get_balance()))
print("User 2 Balance: {}/-".format(user_2.get_balance()))

#OUTPUT
'''
User 1 Balance: 250/-
User 2 Balance: 100/-
Transferring 50/- from User 1 to User 2
User 1 Balance: 200/-
User 2 Balance: 1
'''

#example - 2
#CODE

class BankAccount:
    def __init__(self, account_number):
        self.account_number = str(account_number)
        self.balance = 0

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")

    def deposit(self, amount):
        self.balance += amount


def transfer_amount(acc_1, acc_2, amount):
    acc_1.withdraw(amount)
    acc_2.deposit(amount)


user_1 = BankAccount("001")
user_2 = BankAccount("002")
user_1.deposit(25)
user_2.deposit(100)

print("User 1 Balance: {}/-".format(user_1.get_balance()))
print("User 2 Balance: {}/-".format(user_2.get_balance()))
transfer_amount(user_1, user_2, 50)
print("Transferring 50/- from User 1 to User 2")
print("User 1 Balance: {}/-".format(user_1.get_balance()))
print("User 2 Balance: {}/-".format(user_2.get_balance()))

#OUTPUT
'''
User 1 Balance: 25/-
User 2 Balance: 100/-
Insufficient Funds
Transferring 50/- from User 1 to User 2
User 1 Balance: 25/-
User 2 Balance: 150/-
'''

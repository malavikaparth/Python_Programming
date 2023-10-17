# A class is a group of variables and functions.
# A class name need not start with a capital letter. Capital is just for readability.
# Functions in a class are defined using def

# EG:

class BankAccount:
    balance = 100  # eg of variable without '_'

    # Constructor should always be named __init__  and first argument self
    def __init__(self):
        self._balance = 0  # Here even before declaring instance variable _balance we are using it
        # This is actually possible in python

    # Creating a function to add amount to bank account.
    # THERE ARE CERTAIN RULES
    # Every method of class should start with self
    # Instance variable is a variable that exist for each and every instance you create for the class

    def addAmount(self, amount):
        self._balance = self._balance + amount

    # Eg of self:
    # If self is not there it is not a method of class
    # If self is not there it becomes function of class
    # The difference between method and function is that, methods can word with data of class but functions cannot

    def withdraw(self, amount):
        self._balance -= amount

    def displayBalance(valve):  # Just to use another variable to represent self
        print(valve._balance)


# Creating Object of Class
# Here we are creating one particular bank account
# This means that b is assignes one instance of class and b can have access to all methods and functions of the class BankAccount
b = BankAccount()  # The constructor (i.e __init__()) will be called every time an obj is created
b.addAmount(100)
# I can access variable of a class outside the class using instance variable
# Thus to represent that this is bad coding i use '_' in front of variable
print(b._balance)  # The line underneath indicates Access to a protected member _balance of a class . This is Wrong code
b.__init__()
b.displayBalance()
# Changing balance and printing balance This is wrong coding
print(b.balance)
b.balance = 0
print(b.balance)
# print(b._balance)
b.addAmount(100)
b.displayBalance()


# EXAMPLE OF CLASS COMPLETE
class BankAccount1:
    def __init__(self, name, password):
        self._owner = name
        self._pwd = password
        self._balance = 0

    def setAmount(self, amount, password):
        if self._authenticate(password):
            self._balance += amount
        else:
            print("wrong password")

    def getAmount(self, password):
        if self._authenticate(password):
            return self._balance, self._owner
        else:
            print("wrong password")

    def _authenticate(self, password):
        return self._pwd == password

    def transferAmount(self, amount, otherAccount, password):  # otherAccount is an object of BankAccount
        if self._authenticate(password):
            self.setAmount(-amount, password)
            otherAccount.setAmount(amount, password)
        else:
            print("wrong password")


b = BankAccount1("Malavika", "Luca")
a = BankAccount1("Luca", "TheBestBabyEver")
b.setAmount(100, "Luca")
a.setAmount(200, "TheBestBabyEver")
print(b.getAmount("Luca"))
print(a.getAmount("TheBestBabyEver"))
b.transferAmount(100, a, "Luca")
print(b.getAmount("Luca"))
print(a.getAmount("TheBestBabyEver"))
# b.authenticate()  # Bad coding because it can be called outside. Thus we are making it private by adding '-'

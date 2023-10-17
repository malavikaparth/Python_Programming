class BankAccount:
    def __init__(self, name, password):
        self._owner = name
        self._pwd = password
        self._balance = 0

    def _authenticate(self, password):
        return self._pwd == password

    def setAmount(self, amount, password):
        if self._authenticate(password):
            self._balance += amount
        else:
            print("Transaction failed")

    def getAmount(self):
        return self._owner, self._balance


# jointAccount is a subclass of BankAccount # So => jointAccount can have all properties of BankAccount
# i.e group Account is a bank account. It will have all attributes and methods of BankAccount
# All IS-A relation
# i,e bmw IS A car
# car HAS A engine t,e engine can be an attribute of class
# IS-A : Subclass
# HAS-A :Attribute

class jointAccount(BankAccount):
    def __init__(self, name, password):
        super().__init__(name,
                         password)  # We are calling this to have all values of bank accout here. i.e mainly to show balance = 0
        self._holder = []
        self._pwd = []
        self.addHolder(name, password)

    def addHolder(self, holder, password):
        self._holder.append(holder)
        self._pwd.append(password)

    def _authenticate(self, password):
        return password in self._pwd

    def __str__(self):
        return self._holder,self._pwd



# Based on which class object used we will call the corresponding function for same name function.
a = BankAccount("abc", 111)
b = jointAccount('def', 222)
c = jointAccount('ghi', 221)
a.setAmount(100, 111)
b.setAmount(100, 222)
c.setAmount(100,221)
print(a.getAmount())
print(b.__str__())
print(c.__str__())

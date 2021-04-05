class BankAccount:
	
	def __init__(self, accountNumber, accountName, balance):
		self.__accountNumber = accountNumber
		self.__accountName = accountName
		self._balance = balance

	def withdraw(self, amount):
		if(amount > 0 and amount <= self._balance):
			self._balance -= amount

	
	def deposit(self, amount):
		if(amount > 0 and amount <= 25000):
			self._balance += amount

	def getBalance(self):
		return self._balance

	def getAccountNumber(self):
		return self.__accountNumber

	def getAccountName(self):
		return self.__accountName

	def __str__(self):
		# return "{}{}{}".format(self.__accountNumber, self.__accountName, self._balance)
		return f"{self.__accountNumber} {self.__accountName} {self._balance}"

class CurrentAccount(BankAccount):
	
	__withdrawlFee = 0.0
	def __init__(self, accountNumber, accountName, balance, withdrawlFee):
		super().__init__(accountNumber, accountName, balance)
		self.__withdrawlFee = withdrawlFee
    
	def withdraw(self, amount):
		if(amount > 0 and amount + self.__withdrawlFee <= self._balance):
			self._balance = self._balance - amount - self.__withdrawlFee

class CreditCard(BankAccount):
	__creditLimit = 0
	def __init__(self, accountNumber, accountName, balance, creditLimit):
		super().__init__(accountNumber, accountName, balance)
		self.__creditLimit = creditLimit

	def withdraw(self, amount):
		if(-self._balance + amount <= self.__creditLimit):
			self._balance = self._balance - amount


a = BankAccount(100, "Hero Alom", 1000.0)
b = CurrentAccount(101, "Moga Alom", 1000, 20.00)
c = CreditCard(102, 'Alom', 0, 50000)
c.withdraw(5001)
c.deposit(2000)
c.withdraw(47000)
print(c)
a.deposit(200)
a.withdraw(100)
# a.balance = 1000
b.deposit(10)
b.withdraw(10)

print(a)
print(b)

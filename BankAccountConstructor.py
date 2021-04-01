class BankAccount:

	def __init__(self, number, name, amount):
		self.__accountNumber = number
		self.__accountName = name 
		self.__balance = amount

	def withdraw(self, amount):
		if(amount > 0 and amount <= self.__balance):
			self.__balance -= amount

	def deposit(self, amount):
		if(amount > 0 and amount <= 25000):
			self.__balance += amount

	def getBalance(self):
		return self.__balance

	def getAccountName(self):
		return self.__accountName

	def getAccountNumber(self):
		return self.__accountNumber


a = BankAccount(100, "Hero Alom", 1000)
a.withdraw(200)
a.deposit(1000)
print(a.getAccountNumber(), a.getAccountName(), a.getBalance())

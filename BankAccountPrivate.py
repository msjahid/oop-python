class BankAccount:
	# private __ , protected _, public these are access modifiers
	# We provide data security/safety using these modifiers
	# we enforce "Encapsulation" with these modifiers
	
	def __init__(self, number, name, amount):
		# Private access modifier
		self.__accountNumber = number
		self.__accountName = name 
		self.__balance = amount

	# methods provide "Abstraction"	
	# We don't need to know how something works
	def withdraw(self, amount):
		if(amount > 0 and amount <= self.__balance):
			self.__balance -= amount

	# In python we call functions
	# as methods		
	def deposit(self, amount):
		if(amount > 0 and amount <= 25000):
			self.__balance += amount

	def getBalance(self):
		return self.__balance

	def getAccountNumber(self):
		return self.__accountNumber

	def getAccountName(self):
		return self.__accountName


a = BankAccount(100, "Hero Alom", 1000)
a.deposit(100)
a.withdraw(200)
print(a.getAccountNumber(), a.getAccountName(), a.getBalance())
# print(a.accountNumber, a.accountName, a.balance)
# Code is not working because of my attribute are private
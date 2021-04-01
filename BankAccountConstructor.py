class BankAccount:

	#constructor
	def __init__(self, number, name, amount):
  # def __init__(self, number=None, name="", amount=None): 
		self.accountNumber = number
		self.accountName = name 
		self.balance = amount

	def withdraw(self, amount):
		if(amount > 0 and amount <= self.balance):
			self.balance -= amount

	def deposit(self, amount):
		if(amount > 0 and amount <= 25000):
			self.balance += amount

	def getBalance(self):
		return self.balance

# We are instantiating object "a"
# object "a" is an instance of class "BankAccount"
# 17 Number line is easier so we have to add Constructor
a = BankAccount(100, "Hero Alom", 1000)
a.deposit(100)
# If you want to allow passing no agruments to the class initiator [line 28-31]
# then you have to define the initiator with default values set to None [above line 5]
# b = BankAccount()
# b.accountNumber = 101
# b.accountName = "Abul Mal"
# b.balance = 2000
a.withdraw(200)
# b.deposit(500)
print(a.accountNumber, a.accountName, a.balance)
# print(b.accountNumber, b.accountName, b.balance)
print(a)
# print(b) 

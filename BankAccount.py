class BankAccount:

	def withdraw(self, amount):
		if(amount > 0 and amount <= deposit):
			self.balance -= amount

	def deposit(self, amount):
		if(amount > 0 and amount <= 25000):
			self.balance += amount

	def getBalance(self):
		return self.balance

a = BankAccount()
a.accountName = "Abul Mal"
a.accountId = 101 
a.balance = 500 
a.deposit(50)
print(a.accountId, a.accountName, a.balance)

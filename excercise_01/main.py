from BankAccount import BankAccount

a = BankAccount("UNCC's Account", 60000)
a.deposit(50)
a.withdraw(23)
print(a.get_balance())
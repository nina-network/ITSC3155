class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, money):
        self.balance = self.balance + money
    
    def withdraw(self, money):
        self.balance = self.balance - money

    def get_balance(self):
        return (f'{self.name} has a balance of ${self.balance}')

person_1 = BankAccount("Serena", 1000)
print(person_1.get_balance())
person_1.deposit(1000)
print(person_1.get_balance())
person_1.withdraw(1000)
print(person_1.get_balance())

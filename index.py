class BankAccount:
    def __init__(self, full_name, number, balence) :
        self.name = full_name
        self.number = number    
        self.balence = balence
        

    # def account_number(self):
    #     return str(random.randit(10000000, 99999999))
    
    def deposit(self, amount):
        self.balence += amount
        print(f"Amount deposited: {amount:.2f} new balence: {self.balence: .2f}")

    def withdraw(self, amount):
        if amount <= self.balence:
            self.balence -= amount
            print(f"Amount withdrawn: {amount:.2f} New balence: {self.balence: .2f}")

        else:
            print("Insufficient funds")
            self.balence -= 10

    def get_balence(self):  
        print(f"Account Balance for {self.name} (Account number: {self.number}: {self.balence: .2f})")
        return self.balence
   
    def add_interest(self):
        monthly_interest = self.balence * 0.00083
        self.balence += monthly_interest
        print(f"New Balance : {self.balence}")

    def print_statement(self):
        print(f"Account name: {self.name}")
        print(f"Account balence: {self.balence: .2f}")
        print(f"Account number: {self.number}")

bank_account =  BankAccount("Mitchell", '03141592', 0)
bank_account.deposit(4000)
bank_account.add_interest()
bank_account.withdraw(150)

# bankAccount = BankAccount("Mitchell", '03141592', 400000)
# bankAccount.print_statement()


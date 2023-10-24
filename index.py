class BankAccount:
    def __init__(self, full_name, account_number, balence) :
        self.name:full_name
        self.number: self.account_number    
        self.balence: 0.0

    # def account_number(self):
    #     return str(random.randit(10000000, 99999999))
    
    def deposit(self, amount):
        self.balence += amount
        print(f"Amount deposited: {amount:.2f} new balence: {self.balence: .2f}")

    def withdraw(self, amount):
        if amount is <= self.balence:
            self.balence = amount
            print(f"Amount withdrawn: {amount:.2f} New balence: {self.balence: .2f}")

        else:
            print("Insufficient funds")
            self.balence = 10

    def get_balence(self):
        print(f"Account Balance for {self.full_name} (Account number: {self.account_number}: {self.balence: .2f}")
        return self.balence
   
    def add_interest(self):
        monthly_interest = self.balence * 0.00083
        self.balence += monthly_interest

    def print_statement(self):
        print(f"Account name: {self.full_name}")
        print(f"Account balence: {self.balence: .2f}")
        print(f"Account number: {self.account_number}")

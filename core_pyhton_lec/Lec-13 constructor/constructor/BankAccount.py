#Creation of simeple application

class BankAccount:
    def __init__ (self,initialAmt,accHolder):
        self.balance=initialAmt
        self.name=accHolder
        print("Account is created")
        print(f"Account created for '{self.name}' with Opening balance {self.balance:.2f}")

class Customer:
    def __init__(self, name, surname, tc_identification, phone):
        self.name=name
        self.surname=surname
        self.tc_identification=tc_identification
        self.phone=phone

    def display_information(self):
        print(f"Name:{self.name}")
        print(f"Surname: {self.surname}")
        print(f"TR ID: {self.tc_identification}")
        print(f"Phone:{self.phone}")

class Account(Customer):
    def __init__(self, customer, account_number, balance):
        super().__init__(customer.name, customer.surname, customer.tc_identification, customer.phone)
        self.account_number=account_number
        self.balance=balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been withdrawn. New balance: {self.balance}")


    def money_check(self, amount):
        if self.balance >= amount:
            self.balance-=amount
            print(f"{amount} has been withdrawn. New balance:{self.balance}")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

customer=Customer("John", "Doe", "12345678911", "555-123-4567")
account=Account(customer, "123456789", 1000)
print("Customer Information:")
customer.display_information()

print("\nAccount Operations:")
account.display_balance()
account.deposit(500)
account.money_check(300)
account.money_check(1500)
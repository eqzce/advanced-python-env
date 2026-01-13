class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
            return
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    owner = input("Enter owner name: ")
    balance = float(input("Enter initial balance: "))

    account = BankAccount(owner, balance)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Balance\n4. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            amount = float(input("Amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            print("Balance:", account.get_balance())
        elif choice == "4":
            break

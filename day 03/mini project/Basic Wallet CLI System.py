class Wallet:
    def __init__(self, name, balance):
        self.name = name
        self.history = []
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("invalid")
        else:
            self.__balance += amount
            self.history.append(f"deposited {amount}")

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            print("invalid")
        else:
            self.__balance -= amount
            self.history.append(f"withdraw {amount}")

    def get_balance(self):
        return self.__balance

    def show_history(self):
        for record in self.history:
            print(record)

    def transfer(self, amount, receiver_wallet):
        if amount <= 0 or amount > self.__balance:
            print("invalid transfer")
            return

        self.__balance -= amount
        self.history.append(f"Transferred {amount} to {receiver_wallet.name}")

        receiver_wallet.deposit(amount)
        receiver_wallet.history.append(f"Received {amount} from {self.name}")

Wallets = []

def findwallet():
    name = input("Wallet name: ")

    for wallet in Wallets:
        if wallet.name == name:
            return wallet

    print("Wallet not found")
    return None

def createwallet():
    name = input("Wallet name: ")
    balance = int(input("Initial balance: "))

    new_wallet = Wallet(name, balance)
    Wallets.append(new_wallet)

    print(f"Wallet '{name}' created successfully!")


def deposit():
    wallet = findwallet()
    if wallet:
        amount = int(input("Amount to deposit: "))
        wallet.deposit(amount)


def withdraw():
    wallet = findwallet()
    if wallet:
        amount = int(input("Amount to withdraw: "))
        wallet.withdraw(amount)


def transfer():
    print("Sender wallet:")
    sender = findwallet()
    if not sender:
        return

    print("Receiver wallet:")
    receiver = findwallet()
    if not receiver:
        return

    amount = int(input("Amount to transfer: "))
    sender.transfer(amount, receiver)


def show_balance():
    wallet = findwallet()
    if wallet:
        print("Balance:", wallet.get_balance())


def show_history():
    wallet = findwallet()
    if wallet:
        wallet.show_history()



def main():
    while True:
        print("\n===== WALLET SYSTEM =====")
        print("1. Create Wallet")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Show Balance")
        print("6. Show History")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            createwallet()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            show_balance()
        elif choice == "6":
            show_history()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")



main()
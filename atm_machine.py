# This is a simple program for ATM machine which allows users to Check balance,
# withdraw amount, deposit amount and exit the program

class ATM:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def check_balance(self):
        return self.balance

    def get_statements(self):
        # statements consist of:
        # all last transaction like deposit and withdraw
        return self.transactions

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'Deposited {amount} Taka')
        return f'''
Amount {amount} has been deposited to your account.
Your new Balance is {self.balance}
        '''

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f'Withdrawn {amount} Taka')
            return f'''
Amount {amount} has been withdrawn from your account.
New Balance: {self.balance}
        '''
        else:
            return f'Sorry, insufficient balance.'


def main():

    atm = ATM()
    pin = 1234
    invalid_pin_count = 1

    print("Welcome to the ATM service of IBBL")

    while True:
        given_pin = int(input("Enter your PIN: "))

        if given_pin == pin:
            print('''
--------- MENU -----------

1. Check Balance
2. Deposit
3. Withdraw
4. Statements
5. Exit
                    ''')

            choice = int(input("Enter choice: "))

            if choice == 1:
                print(f'Your current balance is {atm.check_balance()}')
            elif choice == 2:
                amount = float(input("Enter the amount you want to deposit: "))
                print(atm.deposit(amount))
            elif choice == 3:
                amount = float(input('Enter the amount you want to withdraw: '))
                print(atm.withdraw(amount))
            elif choice == 4:
                trans = atm.get_statements()
                print(f'{len(trans)} transactions occured.')
                for i in range(len(trans)):
                    print(f'{i + 1}. {trans[i]}')
            elif choice == 5:
                break
            else:
                print('Invalid input.')
        else:
            if invalid_pin_count == 3:
                print("You attempted maximum time. Try again after 30 minutes.")
                break
            else:
                invalid_pin_count += 1
                print("Invalid PIN. Try again.")

if __name__ == "__main__":
    main()



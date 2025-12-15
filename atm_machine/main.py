from core import transactions
from core import auth

def main():
    card = input("Enter your card number: ")
    pin = input("Enter your pin: ")

    if auth.authenticate_user(card, pin):
        print("Authentication successful!")

        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                balance = transactions.check_balance(card)
                print(f"Your balance is: {balance}")

            elif choice == '2':
                amount = int(input("Enter amount to deposit: "))
                transactions.deposit(card, amount)
                print("Deposit successful!")

            elif choice == '3':
                amount = int(input("Enter amount to withdraw: "))
                if transactions.withdraw(card, amount):
                    print("Withdrawal successful!")
                else:
                    print("Insufficient funds!")

            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")
    else:
        print("Authentication failed!")

if __name__ == "__main__":
    main()

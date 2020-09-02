#This code is for basic ATM functions
import random

class Account:
    # Defines ID , balance initialized to zero and Yearly Interest rate
    def __init__(self, id, balance=0, YearlyIR=3.4):
        self.id = id
        self.balance = balance
        self.YearlyIR = YearlyIR

    def Id(self):
        return self.id

    def Balance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


#Creating account
def main():
    accounts = []
    for i in range(1000,9999):
        account = Account(i, 0)
        accounts.append(account)

    # Main code for execution of ATM functions
    while True:
        id = int(input("Enter account pin: "))

        # Check for valid ID number and if entry is more than 3 times, account will be locked and need
        # to contact bank for further details (Took on the next line to follow PEP8)
        for i in range(3):
            while id<1000 or id>9999:
                print("Not a valid account number")
                id = int(input("Reenter Account Number:"))


        while True:

            #ATM basic function display
            print("\n1 - View Balance \n 2 - Withdraw \n 3 - Deposit \n 4 - Exit ")
            Option = int(input("Enter your selection number: "))

            for acc in accounts:
                # Comparing account id
                if acc.Id() == id:
                    accobj = acc
                    break

            # View Balance
            if Option == 1:
                # Printing balance
                print(accobj.Balance())

            # Withdraw
            elif Option == 2:
                # Take the amount to be withdrawn
                amt = int(input("\n Enter amount to withdraw: "))
                Verify_withdraw = input("Are you sure to withdraw {}, Yes or No ".format(amt))

                if Verify_withdraw == "Yes" or "yes":
                    print("Verify_withdraw")
                else:
                    break

                if amt < accobj.Balance():
                    # Withdraw Method call
                    accobj.withdraw(amt)
                    # Printing updated balance
                    print("\n New Balance: " + str(accobj.Balance()))
                else:
                    print("\n Action denied, withdrawal amt more than amt in account" + str(accobj.Balance()))

            # Deposit
            elif Option == 3:
                # Reading amount
                amt = float(input("\nEnter amount to deposit: "))
                Verify_deposit = input("Are you sure to deposit {}, Yes or No ".format(amt))

                if Verify_deposit == "Yes" or "yes":
                    # Deposit method call
                    accobj.deposit(amt)

                    print("\n Updated Balance: " + str(accobj.Balance()))
                else:
                    break
            #Exit
            elif Option == 4:
                print("\nTransaction is now complete.")
                print("\nTransaction number: ", random.randint(999999, 1000000000))
                print("\nThanks for choosing us as your bank")
                exit()

            else:
                print("\n Invalid selection/choice")

# Calling Main function
main()
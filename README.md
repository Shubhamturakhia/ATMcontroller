# ATMcontroller

This is a basic ATM controller with functions of 
1. Input the Account pin 
2. View Balance
3. Deposit amount 
4. Withdraw amount
5. Exit and create Transaction Id 

The python code creates a class Account to define the basic variables such as ID, Withdraw, Deposit 

## Main function 

The main function asks for entering the 4 digit account pin for the user (it can be extended to verify with database of accounts)
It also gives number of attempts for rentering the Account pin.

It asks for 4 options;
1. View Balances
2. Withdraw
3. Deposit
4. Exit 

Functions considered:
a. The main function remains active as far as the user is using the options and does not go ahead with the 4. Exit() option

b. The withdraw option also checks for the amount to not exceed the account balance limit

c. Transaction Id is created for each exit which is done by the user (this can be improved to store in the database buffer so that user can verify the transaction whenever he/she wants and can be updated on the user account)

d. It also checks for number of times the pin is reentered and also locks the account authentication if it exceeds a threshold (set for 3 attempts here can be changed) 

e. Authentication checks for confirming the withdrawal adn deposit amounts.

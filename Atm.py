print("Welcome to the ATM Services")
account_number=int(input("Enter account number: "))
atm_pin=int(input("Enter pin number: "))
user_account_num=12345
user_atm_pin=9876
user_balance=6000
transcations=[]
while user_account_num!=account_number and user_atm_pin!=atm_pin:
    print("Invalid account number or atm pin..Try again")
    account_number = int(input("Enter account number: "))
    atm_pin = int(input("Enter pin number: "))
else:
    print("Successfuuly Login")
while(True):
    print("1.Check amount")
    print("2.Deposite amount")
    print("3.Withdraw amount")
    print("4.View transaction history")
    print("5.Exit")
    option=input("enter ur choice: ")
    if option=='1':
        print("Amount in ur account is",user_balance)
    elif option=='2':
        amount=int(input("Enter the amount: "))
        while amount<0:
            print("Deposite money should be more than 0")
            amount = int(input("Enter the amount: "))
        else:
            user_balance+=amount
            transcations.append(f"Deposied amount {amount}")
    elif option=='3':
        withdraw=int(input("Enter the amount you want to withdraw: "))
        while withdraw > user_balance:
            print("Insufficient balance")
            withdraw = int(input("Enter the amount you want to withdraw: "))
        else:
            user_balance-=withdraw
            transcations.append(f"Withdrawn amount of{withdraw}")
    elif option=='4':
        print(transcations)
    elif option=='5':
        print("Thank you ")
        break
    else:
        print("Invalid option ..Choose correct option")






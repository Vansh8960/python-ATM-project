import time

balance = 5000
transactions = []
def new():
    choicee = input("Do you wish to see anything else (y/n) ").lower()

    if choicee == "y":
        return True
    else:
        exit()

def balance_check():
    print(f"Your current balance is: ₹{balance}")
    time.sleep(0.5)
    new()

def depo_fn():
    global balance 
    add = int(input("Enter the amount you want to deposit: "))    
    if add > 0:
        balance = balance + add
        print(f"You have deposited ₹{add} and your new balance is ₹{balance}")
        transactions.append(f"Deposited {add}")
        new()

def withdraw_fn():
    global balance
    withdraw = int(input("Enter the amount you want to withdraw: "))
    if withdraw <= balance and withdraw >0 :
        balance = balance - withdraw
        transactions.append(f"Withdraw {withdraw}")
        print(f"You have withdrawn ₹{withdraw}..... Your updated balance is ₹{balance}")
        new()
    elif withdraw > balance:
        print("Amount not available in your account")
        new()
    else:
        print("Please enter positive amount")
        withdraw_fn()
    
def trans():
    global transactions
    print("========== Transaction History =========")
    count = 1
    for i in transactions:
        print(f"{count}.{i}")
        count = count +1
        new()


def atm():
            
            # transactions = []
            while True:
                time.sleep(1)
                print("========= Welcome to ATM =========")
                time.sleep(1)
                print("Please Enter your Choice")
                print(" 1. Check Balance \n 2. Deposit \n 3. Withdraw \n 4. Transation History \n 5. Exit")
                time.sleep(1)

                choice = int(input("Enter your choice Number: "))
                
                ### Working with choices
                ### Balance
                if choice == 1:
                    balance_check()

                ###DEPOSIT
                elif choice == 2:
                    depo_fn()
            
                   
                ###Withdraw
                elif choice == 3:
                    withdraw_fn()
                
                ### Transaction History
                elif choice == 4:
                    trans()

        
                ###Exit
                elif choice == 5:
                    print("     Thank You for using our ATM........ \n     Have a Good Day Ahead")
                    break
               
                ### Invalid Choice
                else:
                    print("Invalid Choice , Please try again")     
                    break


attempts = 0          
while attempts <=3:
    pin = int(input("Enter your pin: "))
     
    if pin == 1234:
        print("Checking Your pin..................................")
        atm()
    else :
        attempts += 1
        print(f"Wrong Pin, try again \n you have {3-attempts} attempts left")
        if attempts == 3:
            print("Too many wrong attempts \nExiting.........")
            exit()
        


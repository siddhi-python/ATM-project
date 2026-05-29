def check_balance(balance):
    print("Balance is", balance)

def deposit(balance, amount):
    return balance + amount

    f.open("history.txt","a")
    f.write(f"Deposited{amount}\n")
    f.close()

def withdraw(balance, amount):
    if amount <= 0:
        print("Invalid amount")
        return balance
    elif amount > balance:
        print("Insufficient balance. Available:", balance)
        return balance
    else:
        print("₹", amount, "withdrawn successfully")
        return balance - amount
    
        f.open("history.txt","a")
        f.write(f"withdraw{amount}\n")
        f.close()    


balance = 1000
correct_pin = "1234"
attempts = 0

# PIN check
while attempts < 3:
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Access Granted ✅")
        break
    else:
        print("Wrong PIN ❌")
        attempts += 1

if attempts == 3:
    print("Too many wrong attempts,Card Blocked 🚫")
    exit()

# ATM menu
while True:
    print("\n==== ATM MENU ====")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. view history")
    print("5.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance(balance)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        if amount <= 0:
            print("Invalid amount")
        else:
            balance = deposit(balance, amount)
            print("Updated balance is", balance)

    elif choice == "3":
        amount = int(input("Enter amount: "))
        balance = withdraw(balance, amount)
        print("Updated balance is", balance)

    elif choice == "4":
        f=open("history.txt","r")
        print(f.read())
        f.close()
        break
    elif choice =="5":
        print("Thank you! 🙏")
        break

    else:
        print("Invalid choice")
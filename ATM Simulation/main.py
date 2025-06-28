import csv
import time


def main_menu():
    print("""
    1. Balance Check
    2. Deposit
    3. Withdraw
    4. Add User
    5. Exit
          """)

    while True:
        choice = input("Enter your choice: ")
        if choice in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("enter a valid choice")

    if choice == "1":
        balance_Check()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        add_user()

    elif choice == "5":
        close()

    else:
        print("Error encountered")


def balance_Check():
    name = input("What is your name ")
    balance = authenticate(name)
    print(" Your Balance Is: ", balance)
    print("")
    main_menu()


def deposit():
    name = input("What is your name ")
    balance = authenticate(name)

    deposit = int(input("How much money are you depositing: "))

    new_balance = balance + deposit

    with open("users_balance.csv", "w") as file:
        fieldnames = ["name", "password", "balance"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({"balance": new_balance})
        print("Balance updated sucessfully")
        print("New balance is ", new_balance)  # faster to do it this way than do call the sub routine again
        print("")
        main_menu()


def withdraw():
    print("")
    name = input("What is your name ")
    balance = authenticate(name)
    while True:
        withdraw = int(input("How much money are you Withdrawing: "))

        if withdraw > balance:
            print("You dont have that much money")
        else:
            break

    new_balance = balance - withdraw

    with open("users_balance.csv", "w") as file:
        fieldnames = ["name", "password", "balance"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({"balance": new_balance})
        print("Balance updated sucessfully")
        print("New balance is ", new_balance)  # faster to do it this way than do call the sub routine again
        print("")
        print("")
        main_menu()


def add_user():
    name = input("Enter your name: ")
    password = input("What would you like your password to be: ")
    balance = int(input("How much money would like to deposit: "))

    with open("users_balance.csv", "w") as file:
        fieldnames = ["name", "password", "balance"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({"name": name, "password": password, "balance": balance})
        main_menu()


def close():
    print("logging off")
    time.sleep(1)  # looks nicer this way
    print("Good bye")
    quit()


def authenticate(name):
    tries = 0

    with open("users_balance.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:

            while True:
                password = input("Enter your password")
                if name == row[0].strip() and password == row[1].strip():
                    print("authenitcation sucessful")
                    return int(row[2].strip())  # retunrs the balance so that it can be used later

                elif name == row[0].strip():
                    print("password is wrong")
                    tries = tries + 1
                    print("You have ", 3 - tries, " attempt remaining ")

                    if tries == 3:
                        print("Program will close for security reason")
                        quit()
                elif name != row[0].strip():
                    print("name does not exist")
                    print("The name doesnt exist , we will create you an account")
                    print("")
                    add_user()


main_menu()

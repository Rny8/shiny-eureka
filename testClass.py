import time

class User():
    def __init__(self, name):
        self.name = name

class Bank(User):
    def __init__(self, name):
        super().__init__(name)
        self.balance = 0

    def deposit(self, amount):
        self.amount = int(amount)
        self.balance = int(self.balance) + amount
        print(f"Account balance has been updated!: $ {self.balance}")

    def withdraw(self, amount):
        self.amount = int(amount)
        self.balance = int(self.balance) - amount
        print(f"Account balance has been updated!: $ {self.balance}")


userData1 = input("What is your name?: ")
user1 = Bank(userData1)

def loadData():
    checkingBalance = open("Data.txt", "r")
    savedBalance = checkingBalance.read()
    user1.balance = savedBalance
    checkingBalance.close()

def saveData():
    fileData = open("Data.txt", "w")
    fileData.write(str(user1.balance))
    fileData.close()

loadData()

bal = int()

def banking():

    def debt():
        if int(user1.balance) < 0:
            print("You are in-debt!")
            user1.balance = 0
            saveData()
            print(f"You have been given a loan... new balance is: {user1.balance}")

    global saveData
    global bal
    time.sleep(0.5)
    userChoice = input(f"Hello!: {user1.name}, press: D for deposit, C to check bal, W for withdraw, Q for quit: ")

    if userChoice.lower() == "d":
        print("You have chosen to make a deposit!")
        userDeposit = int(input("How much would you like to deposit?: "))
        user1.deposit(userDeposit)
        time.sleep(0.5)
        print("WARNING: CLOSING THIS PROMPT WITHOUT PRESSING Q TO QUIT WILL RESULT IN DATA LOSS")
        saveData()
        banking()
    elif userChoice.lower() == "q":
        print("Securing data... Closing")
        time.sleep(0.5)
        fileData = open("Data.txt", "w")
        fileData.write(str(user1.balance))
        fileData.close()
        exit()
    elif userChoice.lower() == "c":
        print("Loading data...")
        time.sleep(1)
        print(f"Your checking account balance is...: ${user1.balance}")
        debt()
        banking()
    elif userChoice.lower() == "w":
        print("You have chosen to withdraw!")
        time.sleep(1)
        userWithdraw = int(input("How much would you like to withdraw?: "))
        user1.withdraw(userWithdraw)
        saveData()
        print(f"You have withdrawn: ${userWithdraw}")
        time.sleep(0.5)
        print(f"Leftover balance is: ${user1.balance} ")
        debt()
        banking()
    elif userChoice.lower() == "clear":
        user1.balance = 0
        fileData = open("Data.txt", "w")
        fileData.write("0")
        fileData.close()
        print("Data cleared...")
        banking()

        
banking()
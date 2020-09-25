from time import sleep
# Parent class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        sleep(0)
        print("So your name is: ", self.name)
        sleep(0)
        print("So your gender is: ", self.gender)
        sleep(0)
        print("So your age is: ", self.age)
        sleep(0)

# Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, gender, age)
        self.balance = 0

    def deposit(self, amount):
        sleep(0)
        print("Please remember to deposit the money in the form of ₹")
        self.amount = amount
        if self.amount < 0:
            print("This is not possible. This format is not available")
        else:
            self.balance += self.amount
            sleep(0)
            print("Account balance deposited is: ₹", self.amount)

    def withdraw_1(self, withdraw_amount):
        sleep(0)
        print("Please remember to deposit the money in the form of ₹")
        self.withdraw_amount = withdraw_amount
        self.amount -= self.withdraw_amount
        sleep(0)
        print("So now you have deposited: ₹", self.withdraw_amount, " money")


running = True
dictionary = {}
while running:
    sleep(0)
    print("Welcome to our service, dear customer")
    sleep(0)
    print("Thank you for choosing this platform for collecting and depositing your money")
    sleep(0)
    print("So let's start")
    sleep(0)
    print("Press 1 to create a new account")
    sleep(0)
    print("Press 2 to add money")
    sleep(0)
    print("Press 3 to withdraw money")
    sleep(0)
    print("Press 4 to view balance")
    sleep(0)
    print("Press 5 to quit")
    input_string = input()
    if input_string == "1":
        sleep(0)
        print("Ok, so now you want to create a new account")
        sleep(0)
        print("For that there are some requirements. These are your full name, age, gender")
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        gender = input("Enter your Gender: ")
        dictionary[name] = Bank(name, gender, age)
        dictionary[name].show_details()
        sleep(0)
        print("These details are registered.")

    if input_string == "2":
        name = input("So as you have logged in with a name, can you please tell me your full name again. ")
        sleep(0)
        print("Checking your account details...")
        try:
            balance = int(input("Enter your balance. "))
            dictionary[name].deposit(balance)
            sleep(0)
            print("Now your balance is being deposited. ")
        except:
            sleep(0)
            print("It seems that you haven't logged in yet. Please login again.")

    if input_string == "3":
        balance = float(input("Enter the balance which you want to withdraw. "))
        name = input("So as you have logged in with a name, can you please tell me your full name again. ")
        sleep(0)
        print("Checking your account details")
        if balance <= dictionary[name].amount:
            try:
                dictionary[name].withdraw_1(balance)
            except:
                sleep(0)
                print("It seems that you don't have any account. So please login again")

        else:
            print("You don't have enough balance to get money!")

    if input_string == '4':
        try:
            name = input("Enter your full name: ")
            print("Your balance is ", dictionary[name].amount)
        except:
            print("It seems that you haven't registered yet. You need to register again.")

    if input_string == '5':
        running = False

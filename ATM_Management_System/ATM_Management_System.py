"""
ATM MANAGEMENT SYSTEM
Features:
-Create Account
-Secure Login
-Deposit Money
-Withdraw Money
-Balance Enquiry
-Change Pin
-File Handling
-Exception Handling
"""
#ATM class containing all banking operations
class ATM:
    #Initialize account details.
    def __init__(self,account_no,name,age,password,balance):
        self.account_no=account_no
        self.name=name
        self.age=age
        self.password=password
        self.balance=balance
    #Deposit money and update the balance in the file
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(amount," is deposited successfully")
        L = []
        f = open("Accounts.txt", "r+")
        for line in f:
            data = line.strip().split(",")
            if len(data) < 5:
                continue
            L.append(data)
        for i in L:
            if (i[0] == self.account_no):
                i[4] = self.balance
                break
        f.close()
        f = open("Accounts.txt", "w")
        for i in L:
            f.write(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n")
        f.close()
    # Withdraw money and update the balance in file
    def withdraw(self,amount):
        if self.balance<amount:
            print("Invalid Value, You dont have sufficient balance in your account.")
        else:
            self.balance=self.balance-amount
            print(amount," is withdrawn successfully")
            L=[]
            f = open("Accounts.txt", "r+")
            for line in f:
                data = line.strip().split(",")
                if len(data)<5:
                    continue
                L.append(data)
            for i in L:
                if (i[0] == self.account_no):
                    i[4] = self.balance
                    break
            f.close()
            f = open("Accounts.txt", "w")
            for i in L:
                f.write(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n")
            f.close()
    #Display the balance in your account
    def enquiry(self):
        print("Your bank balance is ",self.balance)
    # Change the pin of the account and update it in file
    def change_pin(self,pin1):
        self.password=pin1
        print("Your pin has been changed successfully")
        L=[]
        f=open("Accounts.txt","r+")
        for line in f:
            data=line.strip().split(",")
            if len(data)<5:
                continue
            L.append(data)
        for i in L:
            if(i[0]==self.account_no):
                i[3]=pin1
                break
        f.close()
        f=open("Accounts.txt","w")
        for i in L:
            f.write(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n")
        f.close()
    #Generate unique account number in sequential manner
def generate_account_number():
    try:
        with open("Accounts.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                return 1001
            last_line = lines[-1].strip()
            try:
                last_account = int(last_line.split(",")[0])
                return last_account + 1
            except (ValueError, IndexError):
                return 1001
    except FileNotFoundError:
        return 1001

# Create bank account after validating user inputs and add  it in our file
def create_account():
    name = input("Enter your full Name:-")
    while True:
        try:
            age = int(input("Enter your age:-"))
            if age>18:
                break
            else:
                print("Age must be greater than 18.")
        except ValueError:
            print("Enter valid age")
    while True:
        try:
            pin = int(input("Enter your pin:-"))
            if pin>=1000 and pin<=9999:
                break
            else:
                print("Pin must be 4-digit number.")
        except ValueError:
            print("Enter pin which is integers.")
    while True:
        try:
            balance = int(input("Enter your  initial balance:-"))
            if balance>=0:
                break
            else:
                print("Enter Valid balance.")
        except ValueError:
            print("Enter valid balance")
    account_no=generate_account_number()
    print("Your account number is:-",account_no)
    f = open("Accounts.txt", "a")
    f.write(f"{account_no},{name},{age},{pin},{balance}\n")
    f.close()


print("-------WELCOME TO THE BANK--------")
print("---------:PLEASE ENTER YOUR CHOICE:------")
print("1:- To create Account","2:- For Login","3:- For Exit the process")

# Take the input from the user
# 1 To create account  , 2 To login in our account , 3 To exit
while True:
    while True:
        try:
            a=int(input("Enter your choice:--"))
            break
        except ValueError:
            print("Please enter valid number.")

#Create new account by calling create_account() function
    if a==1:
        create_account()
#Login process by accepting account number and pin
    elif a==2:
        # Takes input of account number and then searches it in the file.
        account_found=None
        while True:
            try:
                a1=int(input("Enter your account Number:--"))
                break
            except ValueError:
                print("Enter valid Account Number.")
        f=open("Accounts.txt","r")
        for line in f:
            data=line.strip().split(",")
            try:
                if int(data[0])==a1:
                    account_found=data
                    break
            except (ValueError, IndexError):
                continue
        f.close()
        # If present then it will take password input else it will tell you to make a new account
        if account_found:
            while True:
                try:
                    b=int(input("Enter your password:-"))
                    break
                except ValueError:
                    print("Enter valid password")
            # If password matches then it will do operations like withdraw , deposit etc.
            if b!=int(account_found[3]):
                print("Invalid Password")
                continue
            else:
                #Object has been created for ATM.
                Obj1=ATM(account_found[0],account_found[1],int(account_found[2]),int(account_found[3]),int(account_found[4]))
                while True:
                    print("----:PLEASE ENTER YOUR CHOICE:---")
                    print("For deposit enter 1")
                    print("For withdraw enter 2")
                    print("For enquiry enter 3")
                    print("To change your pin enter 4")
                    print("To exit the process enter 5")
                    while True:
                        try:
                            k = int(input())
                            break
                        except ValueError:
                            print("Enter integer value.")
                    print("You choose option ", k)
                    # Deposit money in the account
                    if k == 1:
                        while True:
                            try:
                                amount = int(input("Enter amount you want to deposit:-"))
                                if amount>0:
                                    Obj1.deposit(amount)
                                    break
                                else:
                                    print("Amount must be greater than 0.")
                            except ValueError:
                                print("Enter Valid Balance.")
                    # Withdraw money from the account
                    elif k == 2:
                        while True:
                            try:
                                amount = int(input("Enter amount you want to withdraw:-"))
                                if amount>0:
                                    Obj1.withdraw(amount)
                                    break
                                else:
                                    print("Amount must be greater than 0.")
                            except ValueError:
                                print("Enter Valid Balance.")
                    # To see current balance
                    elif k == 3:
                        Obj1.enquiry()
                    # To change password of the account by 1st accepting old password and then it will let you enter new password
                    elif k == 4:
                        while True:
                            try:
                                a2=int(input("Enter your old pin:-"))
                                break
                            except ValueError:
                                print("Enter valid pin!")
                        if (a2==Obj1.password):
                            while True:
                                try:
                                    new_pin = int(input("Enter new pin you want:--"))
                                    if new_pin>=1000 and new_pin<=9999:
                                        Obj1.change_pin(new_pin)
                                        break
                                    else:
                                        print("Enter 4 digit pin.")
                                except ValueError:
                                    print("Enter valid interger 4 digits pin")
                        else:
                            print("WRONG PASSWORD CANT CHANGE")
                            continue
                    elif k == 5:
                        print("Your process has been over.")
                        break
                    else:
                        print("Invalid Option")
                        print("Choose number from 1 to 5")
        else:
            print("-----Your Account is not there in our dataset please create your account-----")
            create_account()
    # To exit main loop
    elif a==3:
        print("Thank you for trusting us. Have a nice Day :)")
        break
    else:
        print("Invalid Choice")


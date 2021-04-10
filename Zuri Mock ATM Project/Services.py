import random 
from datetime import datetime
import time


    
def init():
    isvalidOptionSelected = False
    print("welcome to Access Grant Bank")

    while isvalidOptionSelected == False:
        haveAccount = int(input("""Do you have an account with us ?
 Enter 1 (Yes)
 Enter 2 (No)
        \n """))
        if(haveAccount == 1):
            isvalidOptionSelected = True
            login()


        if(haveAccount == 2):
            isvalidOptionSelected = True
            register()

        else:
            print("Invalid Selection")
            init()

def register():
    print("You are welcome to the registeration page")
    email =  str(input("What is your email address: \n" ))
    firstname =  str(input("Please enter your First Name : \n " ))
    lastNAme =  str(input("Please enter your Last Name : \n" ))
    phoneNumber =  str(input("What is your  Phonenumber: \n" ))
    password = str(input("Please do enter New password: \n" ))
    confirmPassword = input("Please do confirm your password? \n")
    password = confirmPassword

    accountNumber = generateAccountNo()
 
    database[accountNumber] = [email,firstname,lastNAme,phoneNumber,password]


    
    print("Please do wait for 3 seconds, Your account is being created")
    time.sleep(4)
    print("Your Account has been created")
    time.sleep(2)
    login()

database = {}

def generateAccountNo():
    for userDetails in database.items():
        firstName = userDetails[1]
        print(firstname + "Please do wait for 10 seconds while we generate your account number for you")
        time.sleep(5)
        data =  random.randrange(0000000000, 8888888888)
        return data
         

def getAccountNumber():
    
        pass
    
    



def login():
    print("******Login Portal******")
    isLoginSuccessfull = False

    while isLoginSuccessfull == False:
        userIdFromUser =  str(input("You are welcome to the ATM, please enter your User Id to login: \n "))
        password = input("What is your Password \n")
 

        for accountNumber, userDetails in database.items():
            if( userIdFromUser == userDetails[0] or accountNumber):
                if(userDetails[4] == password  ):
                    isLoginSuccessfull = True
                    print("you are welcome " + userDetails[1] + "Your Login datetime stamp is:", datetime.now())

        print("invalid Account or Password")
    bankOperations()


def bankOperations():
    for accountNumber, userDetails in database.items():
        print("You are welcome to Operations " + userDetails[1])

    newBalance = ""
    Amount = 0
    options = int(input("""
        Select Option 1 : Withdraw money
        Select Option 2 : Deposit money
        Select Option 3 : For Complaints
        Select Option 5 : End Session
        \n"""))


    if options == 1:
        deposit = int(input("How much will you like to withdraw: "))
        newBalance = Amount - deposit
        print("Please take your cash")
        data = int(input("""Select 1 to execute another Operation 
Select 2 to exit the program \n"""))
        if data == 1:
            login()
        elif data == 2:
            logout()
        else:
            print ("invalid input")
            logout()


    elif options == 2:

        credit = int(input("How much will you like to deposit: "))
        newBalance = Amount + credit
        print("""
            Credit Transaction successful
            Your new balance is #""" + str(newBalance))
        data1 = int(input("""Select 1 to execute another Operation 
Select 2 to exit the program \n"""))
        if data1 == 1:
            login()
        elif data1 == 2:
            logout()
        else:
            print ("invalid input")
            logout()


    elif options == 3:
        str(input("What issue would you like to report? "))
        print("Thank you for contacting us, We will do our best to resolve the complaints ASAP")
        data2 = int(input("""Select 1 to execute another Operation 
Select 2 to exit the program \n"""))
        if data2 == 1:
            login()
        elif data2 == 2:
            logout()
        else:
            print ("invalid input")
            logout()


    #elif options == 4 :
     #   getAccountNumber()


    elif options == 5 :
        logout()
    else:
        print("Selection not valid")
    
def logout():
    quit()

init()

    

    

    


    
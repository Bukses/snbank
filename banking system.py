import random
from random import randint
import sys
def login():
    while True:
        with open ("staff.txt", "r") as f:
            x = 0
            username = input("Username: ")
            password = input("Password: ")
            for i in f.readlines():
                y = i.split (':')
                if len(y) > 1:
                    if y[0] == "Username" and y[1].strip() == username:
                        x += 1
                    elif y[0] == "Password" and y[1].strip() == password:
                        x +=1
            if x == 2:
                print ("\nLog in successful")
                option ()
            else:
                print ("\nWrong Log in details. Try again.\n")

def option():
    print ("\nInput 'yes' in front of your desired option.\nInput 'no' in front of undesired option\n")
    option_a = input ("Create new bank account? ")
    if option_a == "no":
        option_b = input ("Check Account details? ")
        if option_b == "no":
            option_c = input ("Logout? ")
            if option_c == "yes":
                print ("Log out successful")
                login()
            else:
                login()
        else:
            print ("\nPlease type in your generated Account Number")
            account_details()
    else:
        print ("Please supply the following details")
        new_account()
        

def new_account():
    with open ('customer.txt', 'w') as i:
        account_name = input("Account name: ")
        print ("\nSelect account type.\nSavings Account\n\nFixed Deposit Account\n\nCurrent Account\n")
        account_type = input("Account type: ")
        account_email = input ("Account email: ")
        open_bal = input("Opening balance: ")

        num = "310"
        gen_num = ''.join(map(str, random.sample(range(0,9),7)))
        account_num = num+ gen_num
        print (f"\nYour generated Account Number is:\n{account_num} \n")

        i.writelines(f"Details\nAccount Number: {account_num}\nAccount Name: {account_name}\nAccount Email: {account_email}\nAccount Type: {account_type}\nOpen Balance: {open_bal}\n*****")
        print ("\nSaved Successfully")
    
    option()


def account_details():
    while True:
        z = (input("Account Number: "))
        fetch = open ('customer.txt','r').read()
        if z in fetch: 
            front = fetch.find("Account Number: "+ z)
            customer = fetch[front:]
            back = customer.find('***')
            customer = customer[:back]
            print (customer)
            option()
            fetch.close()
        else:
            print ("Input correct Account Number")
    
        





user= input("\nDo you want to proceed to Log in or Close Application?\n\nInput 'yes' for Log in or 'no' for Close Application: ")
while True:
    if user == "yes":
        login()
    elif user == "no":
        print ("You have exited the application")
        exit()
    break








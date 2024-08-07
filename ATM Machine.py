# Banks

# enter your pin, correct pin?

# balance = 3000
# Choose credit cheque savings
# withdraw or deposit

# attempt = int
# CustomerPin = int


# def StartUp():

#     StartUp = input('Ready To Start yes or no? :')
#     if StartUp =='yes':
#         enterpin()
#     elif StartUp =='no':
#         print ('Thank you for banking with us.')
#     else:
#         print ('else number1')
# ()


# def enterpin():
    
#     CustomerPin = 1912
#     pin = (input("Enter Pin: "))
#     if pin == (CustomerPin):
#         print("startatm()")
#     if pin != CustomerPin and i < 3:
#         i += 1
#         enterpin()
#     else:
#         print("Eat Card")    

# # ()
# # CustomerPin = 1912
# # i = 1
# # while i < 6:
# #   StartUp()
# #   i += 1




# #x = 5
# #x += 3  # Equivalent to x = x + 3
# #print(x)  # Output: 8


# # num = int(input("Gimme nummer:  "))

# # for i in range(1, num):
# #     print(i)






import time
CustomerPin = ("1912")
attempts = 0
i = 1

balance = int("300")
#global balance

# def StartUp():
#     global attempts
#     global CustomerPin 
#     global i
#     StartUp = input('Ready To Start yes or no? :')
#     if StartUp =='yes' and i < 3:
#         enterpin()
#     elif StartUp =='no':
#         print ('Thank you for banking with us.')
#     else:
#         print ('else number1')


def enterpin():
    global attempts        # If you use the global keyword, the variable belongs to the global scope:
    global CustomerPin
    global i  
    global pin   
    CustomerPin = ("1912")
    pin = (input("Enter Pin: "))
    i += 1                         # += adds another value with the variable's value and assigns the new value to the variable. | -=, *=, /= does similar for subtraction, multiplication and division.
    if  pin == CustomerPin:
        startatm()
    elif i < 4 and (pin) != CustomerPin:
        enterpin()
    else:
        print("Eat Card")    


def startatm():
    choice1 = (input("credit cheque or savings?"))
    if choice1 == ("credit"):
        CreditAc()
    elif choice1 == ("cheque"):
        ChequAc()
    elif choice1 == ("savings"):
        SavingsAc()
    else:
        startatm()
        

def CreditAc():
    choice2 = (input("deposit or withdrawl "))
    if choice2 == ("deposit"):
        creddep()
    elif choice2 == ("withdrawl"):
        credwithdraw()
    else:
        print("Invalid Response")
        CreditAc()

def ChequAc():
    choice3 = (input("deposit or withdrawl "))
    if choice3 == ("deposit"):
        cheqdep()
    elif choice3 == ("withdrawl"):
        cheqwithdraw()
    else:
        print("Invalid Response")    
        ChequAc()


def SavingsAc():
    choice4 = (input("deposit or withdrawl "))
    if choice4 == ("deposit"):
        savingdep()
    elif choice4 == ("withdrawl"):
        savingwithdraw()
    else:
        print("Invalid Response")  
        SavingsAc()  


def creddep():
    global balance
    choice5 = (input("Enter Deposit Amount :"))
    choice5 = int(choice5)
    if choice5 >0 :
        print("Your new balance is $" + str(int(choice5) + balance)) 
        balance = str(int(choice5) + balance)
    else: 
        print("Please enter a valid amount.")
        creddep()                                                                     #print("You wil be " + str(int(age) + 1) + " in a year.")

def credwithdraw():
    global balance
    choice6 = (input("Enter Withdrawl Amount :"))
    choice6 = int(choice6)
    if choice6 > (balance):
        print("Insufficent funds")
        credwithdraw()
    elif choice6 <= (balance) and choice6 >0 :
        print("Your new balance is $" + str(int(balance) - choice6)) 
        balance = str(int(balance) - (choice6))
    else:
        print("Please enter a valid amount")
        credwithdraw()
        
def cheqdep():
    global balance
    choice7 = (input("Enter Deposit Amount :"))
    choice7 = int(choice7)
    if choice7 >0 :
        print("Your new balance is $" + str(int(choice7) + balance))
        balance = (choice7 + balance)  
    else:
        print("Please enter a valid amount.")
        cheqdep()   

def cheqwithdraw():
    global balance
    choice8 = (input("Enter Withdrawl Amount :"))
    choice8 = int(choice8)
    if choice8 > (balance):
        print("Insufficent funds")
        cheqwithdraw()    
    elif choice8 <= (balance) and choice8 >0 :
        print("Your new balance is $" + str(int(balance) - choice8)) 
        balance = str(int(choice8) + balance) 
    else:
        print("Please enter a valid amount")
        cheqwithdraw()        

def savingdep():
    global balance
    choice9 = (input("Enter Deposit Amount :"))
    choice9 = int(choice9)
    if choice9 >0 :
        print("Your new balance is $" + str(int(choice9) + balance))
        balance = str(int(choice9) + balance)
    else: 
        print("Please enter a valid amount.")
        savingdep()   

def savingwithdraw():
    global balance
    choice10 = (input("Enter Withdrawl Amount :"))
    choice10 = int(choice10)
    if choice10 > (balance):
        print("Insufficent funds")
        savingwithdraw()  
    elif choice10 <= (balance) and choice10 >0 :         
        print("Your new balance is $" + str(int(balance) - choice10))
        balance = str(int(choice10) + balance)  
    else:
        print("Please enter a valid amount")
        savingwithdraw()           



if i < 3:
    print("connecting to bank please wait")
    time.sleep(.5)
    print("establishing secure connection")
    time.sleep(0.5) 
    print(".")
    time.sleep(0.4) 
    print("..")
    time.sleep(0.3) 
    print("...")
    time.sleep(0.2) 
    print("....")
    time.sleep(0.1) 
    print(".....")
    time.sleep(0.09) 
    print("......")
    time.sleep(0.08) 
    print(".......")
    time.sleep(0.07) 
    print("........")
    time.sleep(0.06) 
    print(".........")
    time.sleep(0.05) 



    print("Connection established")


    enterpin()

    
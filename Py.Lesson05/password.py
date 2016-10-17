password=input("Please set your password: ")
user= input("Please set your username: ")
def passCheck():
    wordcheck=input("Please input your password: ")
    usercheck= input("Please input your username: ")
    if password==wordcheck and user==usercheck:
        print("You are granted access!!")
    elif password!=wordcheck and user==usercheck:
        print("Your password is incorrect!")
        passCheck()
    elif password==wordcheck and user!=usercheck:
        print("Your username is incorrect!!")
        passCheck()
    else:
        print("Your username and password are incorrect!")
        passCheck()
passCheck()
              
        
              

num1=float(input("What is your first number: "))
num2=float(input("What is your second number: "))
num3=float(input("What is your third number: "))

def average():
    return(num1+num2+num3)/3

def display():
    print("The average of", num1, ",", num2, ", and", num3, "is", "{:00.5f}".format(average()))

average()
display()
    

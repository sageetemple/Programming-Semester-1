number= int(input("Please enter a number: "))
digits = 0
average = 0

def avDigits():
    num=number
    global digits, average
    while num > 0:
        digits +=1
        average +=digits
        num = int(num/10)
    average= average
    print("The average of the digits in ", number," is ", average)

avDigits()
        

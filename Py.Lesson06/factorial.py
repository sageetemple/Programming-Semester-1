num=int(input("Please enter a number: "))
factorial = 1
def loop():
    for i in range(1,num+1):
        global factorial
        factorial = factorial * i
loop()
print(factorial)

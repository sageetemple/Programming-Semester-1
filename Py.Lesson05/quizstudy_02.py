


num1=7
num2=5
def calcSum(one,two):
    return one+two
def sumPrint(one,two):
    print("The sum of",one," and",two," is", calcSum(one,two))
sumPrint(num1,num2)    

def calcSurf(side):
    return 6*(side**2)

item="Cheeseburger"
price=7.896
def formatR(one,two):
    print("{:<15}......${:0.2f}".format(one,two))
formatR(item,price)

item1=5.675
item2=7.897
def formatr(one,two):
    print("The total cost of your order is ${:5.2f}".format(one+two))
formatr(item1,item2)


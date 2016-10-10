item1= input("What is your first item:")
price1= float(input("What is your first price:"))
item2=input("What is your second item: ")
price2=float(input("What is your second price: "))
item3=input("What is your third item:")
price3=float(input("What is your third price:"))
item4=input("What is your fourth item:")
price4=float(input("What is your fourth price:"))
subtotal = price1+price2+price3+price4
taxmoney= subtotal*.075
discount=0
def discount():
    global discount
    if (subtotal+taxmoney)>=2000:
        discount=(subtotal+taxmoney)*.15
    if (subtotal+taxmoney)<=2000:
        discount=(subtotal+taxmoney)*0
print("\n")    
print("{:<>24}".format(" Receipt"),"{:><20}".format(""))
def displayreceipt(item,price):
    print("{:<10}".format(item),"{:.>30.2f}".format(price))
displayreceipt(item1,price1)
displayreceipt(item2,price2)
displayreceipt(item3,price3)
displayreceipt(item4,price4)
print("\n")
displayreceipt("Subtotal",subtotal)
displayreceipt("Tax",taxmoney)
discount()
displayreceipt("Discount",discount)
total = subtotal-discount+taxmoney
displayreceipt("Total",total)
print("{:_^45}".format("_"),"\n {:*^40}".format("Thank you please come again!!"))


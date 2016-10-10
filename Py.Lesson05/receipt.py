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
def discount():
    (subtotal+tax)*.15
save=(subtotal+tax)>=2000
    
print("{:<>24}".format(" Receipt"),"{:><20}".format(""))
def displayreceipt(item,price):
    print("{:<10}".format(item),"{:.>30}".format(price))
item=item1
price=price1
displayreceipt(item,price)
item=item2
price=price2
displayreceipt(item,price)
item=item3
price=price3
displayreceipt(item,price)
item=item4
price=price4
displayreceipt(item,price)
print("\n")
item="Subtotal"
price=subtotal
displayreceipt(item,price)
item="Tax"
price=taxmoney
displayreceipt(item,price)
if save:
    print("{:<10}".format("Discount"),"{:.>30}".format(discount()))
if not save:
    print("{:*^40}".format("No discount today :("))



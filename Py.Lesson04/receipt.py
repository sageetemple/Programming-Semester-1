

item1=input("Enter item one: ")
price1= float(input("Enter item one's price: "))
item2= input("Enter item two: ")
price2= float(input("Enter item two's price: "))
item3=input("Enter item three: ")
price3=float(input("Enter item three's price: "))
print("\n\n")
print("{:<>15}".format("__"), "Receipt__", "{:>>15}".format(""))
print("\n")
def receipt(item,space,price):
    print("* {:>13}{:.<15}\t{:>5.2f}".format(item," ",price))
item=item1
price=price1
receipt(item," ",price)
item=item2
price=price2
receipt(item," ",price)
item=item3
price=price3
receipt(item," ",price)
print("\n")

def endreceipt(total,space,monies):
    print("* {:>13}{:.<15}\t{:>5.2f}".format(total," ",monies))
total="Subtotal:"
monies=price1 + price2 + price3
endreceipt(total," ",monies)
total="Tax:"
monies= 0.07*(price1+price2+price3)
endreceipt(total," ",monies)
total="Total:"
monies=(price1+price2+price3)+(0.07*(price1+price2+price3))
endreceipt(total," ",monies)
print("\n")
print("{:_^43}".format("_"))
print("     * Thank you for your support *")

                    
                    
                    

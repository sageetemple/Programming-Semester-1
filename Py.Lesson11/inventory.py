import random
class Inventory:
    def __init__(self, iMan, iName, iCat=" ", iPrice=" "):
        self.man=iMan
        self.name=iName
        self.category=iCat
        self.UPC=random.randint(0,1000000)
        self.price=iPrice

    def GetMan(self):
        return self.man
    def GetName(self):
        return self.name
    def GetCat(self):
        return self.category
    def GetUPC(self):
        return self.UPC
    def GetPrice(self):
        return self.price
    def ModCat(newcat):
        self.category = newcat
    def __str__(self):
        return "Inventory Info....\nManufacturer: " + self.man +"\nName: " + self.name +"\nCategory: "+self.category+"\nUPC: "+str(self.UPC)+"\nPrice: "+str(self.price)

def main():
    man= input("Please enter the item manufacturer: ")
    name=input("Please enter the item name: ")
    CP=input("Will you be entering category and price info? [yes/no]")
    if CP=="yes":
        category=input("Please enter the item category: ")
        price = int(input("Please enter the item price: "))
        user1=Inventory(man, name, category, price)
    else:
        user1=Inventory(man, name)
    print("\n",user1.__str__())
main()


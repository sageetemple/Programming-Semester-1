r=float(input("What is your circle's radius: "))
area=0
def calcArea():
    global area
    area = 3.14159*(r**2)
def printArea():
    print("The area of a circle with a radius of", r, "is", "{:00.5f}".format(area))
calcArea()
printArea()

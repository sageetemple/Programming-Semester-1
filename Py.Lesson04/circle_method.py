r=float(input("What is your circle's radius: "))

def calcArea():
    return 3.14159*(r**2)
def printArea():
    print("The area of a circle with a radius of", r, "is", "{:00.5f}".format(calcArea()))
calcArea()
printArea()

length= float(input("What is your rectangle length: "))
width = float(input("What is your rectangle width: "))

def calcPerimfunc():
    return 2*length+2*width
def calcPerim():
    print("Your rectangle is", "{:00.5f}".format(calcPerimfunc()), "sq ft around.")

calcPerimfunc()
calcPerim()

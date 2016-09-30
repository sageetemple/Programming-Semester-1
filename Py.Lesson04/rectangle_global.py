length= float(input("What is your rectangle length: "))
width = float(input("What is your rectangle width: "))
perimeter = 0
def calcPerimfunc():
    global perimeter
    perimeter = 2*length+2*width
def calcPerim():
    print("Your rectangle is", "{:00.5f}".format(perimeter), "sq ft around.")

calcPerimfunc()
calcPerim()

side=float(input("What is your cube's side length: "))
sa=0
def calcSurf():
    global sa
    sa = 6*(side**2)
def printSurf():
    print("The surface area of a cube with side length", side,"is", "{:00.5f}".format(sa))

calcSurf()
printSurf()
    

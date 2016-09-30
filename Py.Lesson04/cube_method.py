side=float(input("What is your cube's side length: "))

def calcSurf():
    return 6*(side**2)
def printSurf():
    print("The surface area of a cube with side length", side,"is", "{:00.5f}".format(calcSurf()))

calcSurf()
printSurf()
    

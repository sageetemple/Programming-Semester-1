import math

class Distance:
    #Constructor
    def __init__(self, x1, y1, x2, y2):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        xOne = x1
        yOne = y1
        xTwo = x2
        yTwo = y2

    #Modifier
    def modDistance(self, newX1, newY1, newX2, newY2):
        self.xOne = newX1
        self.yOne = newY1
        self.xTwo = newX2
        self.yTwo = newY2

    #Acessor
    def getDistance(self):
        distance = math.sqrt((self.xTwo - self.xOne)*(self.xTwo - self.xOne)+ (self.yTwo -self.yOne)*(self.yTwo-self.yOne))
        return distance
def main():
    xOne = int(input("Please enter your first x-coordinate: "))
    yOne = int(input("Please enter your first y-coordinate: "))
    xTwo = int(input("Please enter your second x-coordinate: "))
    yTwo = int(input("Please enter your second y-coordinate: "))

    #Instantiate object

    distance1=Distance(xOne, yOne, xTwo, yTwo)
    print("<<<<<<<<DISTANCE>>>>>>>")
    print("Your distance is {:0.2}".format(distance1.getDistance()))

    distance1.modDistance(4,5,6,7)
    print("<<<<<<<<DISTANCE>>>>>>>")
    print("Your distance is {:0.2}".format(distance1.getDistance()))
main()
    
        

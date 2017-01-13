class Car:
    #Constructor
    def __init__(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t
        paint = p
        interior = i
        engine = e
        tires = t

    #Modifier
    def setCustom(self, newP, newI, newE, newT):
        self.paint = newP
        self.interior = newI
        self.engine = newE
        self.tires = newT

    #Accessors
    def getPaint(self):
        return self.paint

    def getInterior(self):
        return self.interior

    def getEngine(self):
        return self.engine

    def getTires(self):
        return self.tires

def main():
    paint=input("Please enter your paint color: ")
    interior=input("Please enter your interior choice: ")
    engine=input("Please enter your preference for your engine: ")
    tires=input("Please enter your choice of tires: ")
    car1= Car(paint, interior, engine, tires)
    print("Your vehicle is ready... \nPaint:", car1.getPaint())
    print("Interior: ", car1.getInterior())
    print("Engine: ", car1.getEngine())
    print("Tires: ", car1.getTires())

main()

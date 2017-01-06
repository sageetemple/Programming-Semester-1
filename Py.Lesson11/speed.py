class MilesPerHour:
    #Constructor
    def __init__(self, dist,hour,minut):
        self.distance = dist
        self.hours = hour
        self.minutes = minut
        distance=dist
        hours=hour
        minutes=minut
        mph=0

    #Modifier
    def modSpeed(self,newDist,newHour,newMinut):
        self.distance = newDist
        self.hours = newHour
        self.minutes = newMinut
        mph=0

    #Accessor
    def getDistance(self):
        return self.distance

    def MPH(self):
         mph= self.distance / (self.hours + ((self.minutes)/60))
         return mph
    
    def getTime (self):
        return self.hours + (self.minutes)/60
    
def main():
    distance = int(input("Enter your distance: "))
    hours = int(input("Enter the hours spent: "))
    minutes =int( input("Enter the minutes spent: "))
    mph=0

    #Instantiate an object

    distance1 = MilesPerHour(distance, hours, minutes)

    print("<<<<<<<<< SPEED INFO >>>>>>>>")
    print("   ",distance1.getDistance(), "miles in", "{:0.2f}".format(distance1.getTime()), "hours is", "{:0.2f}".format(distance1.MPH()))

    distance1.modSpeed(10, 2, 30)

    print("<<<<<<<<< SPEED INFO >>>>>>>>")
    print("   ",distance1.getDistance(), "miles in", "{:0.2f}".format(distance1.getTime()), "hours is", "{:0.2f}".format(distance1.MPH()))

main()

    

    

    

import random
class User:
    def __init__(self, fName, lName, avat = " "):
        self.firstName = fName
        self.lastName = lName
        self.avatar = avat
        self.userID = random.randint(0,10000000)

    def ModAv(newavat):
        self.avatar = newavat

    def GetAv(self):
        return self.avatar
    def GetF(self):
        return self.firstName
    def GetL(self):
        return self.lastName
    def GetUser(self):
        return self.userID
    def __str__(self):
        return "User Info...\nFirst Name: " + self.firstName+ "\nLast Name: " + self.lastName+ "\nAvatar: " + self.avatar+ "\nUser ID: " + str(self.userID)
def main():
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    avY= input("Would you like a public avatar? Please answer yes or no. ")
    if avY == "yes":
        avatar=input("Please enter your desired avatar name: ")
        user1 = User(firstName, lastName, avatar)
    else:
        user1 = User(firstName, lastName)
    print("\n", user1.__str__())
    
main()

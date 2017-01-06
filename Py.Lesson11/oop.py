class UserNames:
    #Constructor
    def __init__(self, fName, lName, uName):
        self.firstName = fName
        self.lastName = lName
        self.userName = uName

    #Modifier
    def setUserName(self, newUser):
        self.userName = newUser

    #Accessor
    def getfirstName(self):
        return self.firstName
    def getlastName(self):
        return self.lastName
    def getuserName(self):
        return self.userName

def main():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    userName = input("Enter username: ")

    #Instantiate an object
    user1 = UserNames(firstName, lastName, userName)

    print("<<<<<<<< USER INFO >>>>>>")
    print("Name: ", user1.getfirstName(), " ", user1.getlastName())
    print("Username: ", user1.getuserName())

    user1.setUserName("tetm")

    print("<<<<<<<< USER INFO >>>>>>")
    print("Name: ", user1.getfirstName(), " ", user1.getlastName())
    print("Username: ", user1.getuserName())
main()

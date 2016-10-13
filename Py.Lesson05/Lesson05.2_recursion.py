import random
def recursion2():
    guess=int(input("Pick a number between 1 and 10"))
    number = random.randint(1,10)
    print("The number is", number)
    if guess >=1 and guess<=10:
        if guess == number:
            print("The number is right!")
        else:
            print("Wrong!")
    else:
        print("Please make it 1-10")
        recursion2()
recursion2()


def recursion():
    choice = input("Would you like to do some recursion?: ")
    if choice=="Y" or choice == "N":
        if choice =="Y":
            print("Yay! Let's so some recursion!")
        else:
            print("Spoiled the fun!")
    else:
        print("Please enter Y or N")
        recursion()

recursion()


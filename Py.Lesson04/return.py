def cube(side):
    return(side**3)

side = int(input("Enter the side length of your cube: "))

print("Your cube is", cube(side), " cubic inches.")

def format(number):
    output = "{:5.5f}".format(number)
    return output
num1= 1 / 3
print(format(num1))


height=int(input("Enter height in inches: "))
length=int(input("Enter length in inches: "))
width=int(input("Enter width in inches: "))

def vol(height, length, width):
    return((height*width*length)*0.000578704)

print("Your subwoofer volume is ", "{:4.4f}".format(vol(height, length, height)), "ft^3")

num = 8%6
print(num)

one = int(input("Please enter a number: "))
two = int(input("Please enter a second number: "))
even = (one+two) % 2 ==0
if even:
    print((one+two), "is even!")
    
if not even:
    print((one+two), "is odd!")
    

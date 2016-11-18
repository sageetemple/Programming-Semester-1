numbers=[]
for i in range(0,10):
    import random
    i=random.randint(1,100)
    numbers.append(i)
for i in numbers:
    print(i)
output=" "
for i in numbers:
    output += str(i) + " "
print(output+ "\n")

def average(lists):
    average=0
    for i in lists:
        average += i
    return(sums/10)
print("The average of the above numbers is ", int(average(numbers)))

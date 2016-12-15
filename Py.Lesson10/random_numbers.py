import random
numsList=[]
for i in range(0,4):
    numsList.append([])
    for j in range (0,4):
        numsList[i].append(random.randint(1,100))
for value in numsList:
    output=" "
    for num in value:
        output += str(num) + "\t"
    print(output + "\n")

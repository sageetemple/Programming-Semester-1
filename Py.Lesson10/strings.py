go = input("Please input a list of 16 words in a single string: ")
spList = go.split(" ")
wordsList = []
spot = 0
for i in range(0,4):
    output = " "
    wordsList.append([])
    for j in range(0,4):
        wordsList[i].append(spList[spot])
        output += wordsList[i][j] + "\t"
        if spot<=16:
            spot +=1
    print(output)
    

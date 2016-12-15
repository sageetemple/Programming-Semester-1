lettersList = []
lettersList.append(["a", "b", "c", "d"])
lettersList.append(["e", "f", "g", "h"])
lettersList.append(["i", "j", "k", "l"])
lettersList.append(["m", "n", "o", "p"])

for letters in lettersList:
    output= " "
    for letter in letters:
        output += letter + "\t"
    print(output)

print("\nHere is a list of words using split()")
wordsList=[]
go = "father mother eagle house car coffee office make laugh cry photo create"
spList= go.split(" ")
print(spList)
spot = 0 #keeps track of where we are in spList
for i in range(0,3): #handles the columns 
    output = " "
    wordsList.append([]) #creates new index
    for j in range(0,4): #adds new list into the index (rows)
        wordsList[i].append(spList[spot])
        output += "{:15}".format(wordsList[i][j])
        spot += 1
    print(output)

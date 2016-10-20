word=input("Please enter a word:")

def printTri():
    for i in range(0,len(word)):
        print(word[0:i])
printTri()        

for i in range(0,len(word)+1):
    print(word[i])

word="COMPSCI"
print(word[1:4])
print(word[2])
print(word.index("S"))
print(len(word))

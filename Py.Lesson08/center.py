word1=input("Please enter your first word: ")
word2=input("Please enter your second word: ")
word3=input("Please enter your third word: ")

def makeCenter(word):
    if len(word)>=20:
        return word
    else:
        return makeCenter(" "+word+" ")

print(makeCenter(word1))
print(makeCenter(word2))
print(makeCenter(word3))

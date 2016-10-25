word1="Na"
num=4
output=" "
def loop(word,num,output):
    for i in range(0,(num+1)*len(word),len(word)):
        output=output+ str(word[0:i])+" "
    print(output)
loop(word1,num,output)
loop(word1,num,output)
word2="Hey"
num2=3
loop(word2,num2,output)
word3="Goodbye!"
num3=1
loop(word3,num3,output)
print("\n \nDo you know the song?")



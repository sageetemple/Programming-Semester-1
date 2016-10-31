sentence=input("Please enter a string: ")
top=0
while top < sentence.count(" ") >0:
    #slice first part of sentence before first space and then add to rest of sentence without space
    sentence = sentence[0:sentence.index(" ")] + sentence[sentence.index(" ")+1:len(sentence)]
print("Without spaces..." + sentence)



top = 0
sentence=input("Please enter a string: ")
while top<len(sentence):
    print(sentence[top])
    top +=1
    

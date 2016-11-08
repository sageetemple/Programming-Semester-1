word=input("Please enter a word: ")
stop=len(word)
start=0
def tree(word,start,stop):
    if start<=stop:
        print(word[0:start])
        start=start+1
        tree(word,start,stop)
tree(word,start,stop)

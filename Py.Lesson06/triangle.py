string=input("Please enter a word: ")
def loop():
    for i in range(len(string),0,-1):
        print(string[0:i])
loop()


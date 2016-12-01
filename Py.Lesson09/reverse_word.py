words=["hello","okay","cool","yeah","lol"]
print("In order...")
for i in words:
    print(i)
print("\n\nReversed...")
z=0
def reverse(some):
    for i in range((len(some)-1),-1,-1):
        global z
        z=some[i]
        print(z)
reverse(words)
    

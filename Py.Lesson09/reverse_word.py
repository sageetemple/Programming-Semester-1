words=["hello","okay","cool","yeah","lol"]
print("In order...")
for i in words:
    print(i)
print("\n\nReversed...")
def reverse(some):
      for i in range(0,len(some),-1):
            z=some[i]
      output=" "
      output += str(z) + " "
      print(output)
reverse(words)
    

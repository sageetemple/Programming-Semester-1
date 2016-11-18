start=int(input("Please enter your starting number: "))
size=int(input("Please enter your sequence size: "))

seq=[]
for i in range(0,size):
    if i<=1:
        seq.append(start)
    else:
        z=(seq[i-1])+(seq[i-2])
        seq.append(z)
output=" "
for i in seq:
    output += str(i)+" "
print(output)
    
    

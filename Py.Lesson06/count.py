endnum=int(input("Please enter your desired end number: "))
countnum=int(input("Please enter the amount you would like to count by: "))
output=" "
for i in range(countnum,endnum+countnum,countnum):
    output=output + str(i)+" "

print(output)
    

need = int(input("Please enter the number of cookies that you need: "))
batchSize= 25
batch=1
for cookies in range(need, -1, -batchSize):
    print("Cookies Needed: ", cookies)
    print("Batch Number:", batch)
    batch=batch+1

print("Order Up!")







output=" "
for i in range(10,0,-1):
    output=output + str(i) + " "
print(output)


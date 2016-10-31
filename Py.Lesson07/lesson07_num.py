num = int(input("Please enter a number: "))
digits = 0
numb=num
while numb>0:
    digits +=1
    numb = int(numb / 10)

print("There are", digits, " digits in ", num)



number = int(input("Please enter a number: "))

while number > 0:
    #%10 return the last digit on the right of the number
    print (number % 10)
    #dividing by 10 shaves off the last digit on the right
    number= int(number / 10)

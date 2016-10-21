num=int(input("Please enter a number: "))
size=int(input("Please enter the size of your desired table: "))

def loop():
    for i in range(1,size):
        print("{:<10}".format(i),"{:>10}".format(i*num))

loop()


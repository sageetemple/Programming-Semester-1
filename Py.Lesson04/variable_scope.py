#can make var2 and var3 into global variables so can be used anywhere in the function and would delete from under the methods
var2=47
var3=89.1

def method1():
    var2=47
print(var2) #can't because var2 only in method1

def method2():
    var3=89.1
    print(var2)

method2() #can't print var2

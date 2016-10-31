


element1=input("Please enter first element")
electro1=float(input("Please enter electroneg"))
element2=input("Please enter second element: ")
electro2=float(input("Please enter electroneg: "))

def calcBond(one,two):
    if one>two:
        if one-two>=1.7:
            return "ionic"
        else:
            return "covalent"
    else:
        if two-one>=1.7:
            return "ionic"
        else:
            return "covalent"

bond=calcBond(electro1,electro2)
print("The bond between" + element1 + " and " + element2+" is " + bond)


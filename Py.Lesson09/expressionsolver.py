express=input("Please enter a mathematical expression: ")
equation=express.split()

i=0
while i < len(equation):
      if i<len(equation) and (equation[i]=="*" or equation[i]=="/"):
            if equation[i]=="*":
                  equation[i]=(int(equation[i-1])*int(equation[i+1] ))
            else:
                  equation[i]=(int(equation[i-1]) /int(equation[i+1]))
            equation.remove(equation[i-1])
            equation.remove(equation[i])
      i =i+1
i=0
while i < len(equation):
      if i < len(equation) and (equation[i]=="+" or equation[i]=="-"):
            if equation[i]=="+":
                  equation[i]=(int(equation[i-1]) + int(equation[i+1]))
            else:
                  equation[i]=(int(equation[i-1])-int(equation[i+1]))
            equation.remove(equation[i-1])
            equation.remove(equation[i])
      i =i+1
print(equation)



      

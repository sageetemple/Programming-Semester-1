math=input("Enter your Math grade:")
science=input("Enter your Science grade:")

grade=0

def calcPoints(subject):
    global grade
    if subject=="A":
        grade=4.0
    if subject=="B":
        grade=3.0
    if subject=="C":
        grade=2.0
    if subject=="D":
        grade=1.0
    if subject=="F":
        grade=0
gpa = (calcPoints(math))+ (calcPoints(science))
print(gpa)

history=input("Enter your History grade:")
compsci=input("Enter your Computer Science grade:")
english=input("Enter your English grade:")
language=input("Enter your Language grade:")
elective=input("Enter your Elective grade:")

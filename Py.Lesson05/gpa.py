math=input("Enter your Math grade:")
science=input("Enter your Science grade:")
history=input("Enter your History grade:")
compsci=input("Enter your Computer Science grade:")
english=input("Enter your English grade:")
language=input("Enter your Language grade:")
elective=input("Enter your Elective grade:")
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
calcPoints(math)
mathgrade = grade
calcPoints(science)
sciencegrade= grade
calcPoints(history)
historygrade=grade
calcPoints(compsci)
compscigrade=grade
calcPoints(english)
englishgrade=grade
calcPoints(language)
languagegrade=grade
calcPoints(elective)
electivegrade=grade
gpa=(mathgrade+sciencegrade+historygrade+compscigrade+englishgrade+languagegrade+electivegrade)/7
print("Your GPA is", gpa)




height=float(input("Enter your height in inches:"))
weight=float(input("Enter your weight in pounds:"))
bmi=0
condition =0
def calcBMI():
    global bmi,condition
    bmi=(weight*703)/(height)**2
    if bmi<18.5:
        condition="Underweight"
    elif bmi<=24.9:
        condition="Normal"
    elif bmi<=29.9:
        condition="Overweight"
    elif bmi<=34.9:
        condition="Obese"
    elif bmi<=39.9:
        condition="Very Obese"
    if bmi>39.9:
        condition="Morbidly Obese"
    print("Your BMI is:",bmi,"\nYou are",condition)
calcBMI()

    

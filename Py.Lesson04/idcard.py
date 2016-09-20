firstname=input("What is your first name:")
lastname=input("What is your last name:")
title=input("What is your title:")
subject=input("What is your subject:")
school=input("What is your school:")
year=input("What is your school year:")
print("{:*^35}".format("*"))
def card(left,right):
    print("* {:<10}\t{:>18}*".format(left,right))
left=firstname
right=lastname
card(left,right)
left=title
right=subject
card(left,right)
left=school
right=year
card(left,right)
print("{:*^35}".format("*"))


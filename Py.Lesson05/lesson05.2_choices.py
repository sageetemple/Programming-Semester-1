mathorwords = int(input("Would you like to...."+
                        "\n 1. Do a Math Problem"+
                        "\n 2. Answer a question"))
if mathorwords ==1:
    mathanswer=int(input("What is 2 x 2?"))
    if mathanswer ==4:
        print("Correct!!!")
    else:
        print("No cigar!")
else:
    wordanswer=input("Who said the phrase\"Whatever you are,be a good one.\"?")
    if wordanswer=="Abraham Lincoln":
        print("Correct!!!")
    else:
        print("No! Wrong! You lose!!!")
        




number=int(input("Please enter a number:"))

if number > 4:
    print("It meets the first condition")
    if number <=10:
        print("It meets both conditions!!!")

else:
    print("It meets none of the conditions!!")
    

        

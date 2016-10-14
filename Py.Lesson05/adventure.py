def choice():
    choices= input("As you float down a river waiting for rescue you pass by a \"branch\", \"a walkie talkie\", and \"a bag of pebbles\". You are carrying a peanut butter sandwich in one hand and can only pick up one item as you pass by. Which do you take with you? \n")
    a = "branch"
    b = "a walkie talkie"
    c = "a bag of pebbles"
    choice1= a or b
    if choices == choice1:
        if choices==a:
            print("A helicopter spots you and Jackie Chan prepares to rappel out to save you")
            choice2=input("Do you \"shout\", \"flag him down\", or \"continue floating\"?")
            d="shout"
            e="flag him down"
            f="continue floating"
            if choice2==f:
                print("He spots you! You are picked up and given a cup of cocoa!")
            else:
                print("Unbeknowst to you, there were secret ninjas in the trees waiting to take you out and you've alerted them to your location.")
                choice3=input("Do you \"yell\" to alert Mr. Chan or \"get captured\" because you know that you can fight them on land?")
                o="yell"
                l="get captured"
                if choice3==l:
                      print("You have an epic fight and Mr Chan swoops in at the last minute to fly you out of the trees!")
                else:
                      print("The ninjas spot you! They begin their attack! Mr Chan flies over and picks you up, but you get a ninja star lodged in your leg :(")
                      
    elif choices==c:
        choice4= input("You spot an alligator up ahead! Do you go \"right\", \"left\", or \"befriend it\"?")
        x="right"
        y="left"
        z="befriend it"
        if choice4==z:
            print("In exchange for your peanut butter sandwich he agrees to give you a ride to shore and you make it home safe!!")
        else:
            print("He thinks that you want to fight!")
            choice5=input("Do you \"throw your pebbles\" at him, quickly \"construct a white flag\", or \"swim away furiously\"?")
            q="throw your pebbles"
            p="construct a white flag"
            m="swim away furiously"
            if choice5==m:
                print("Unfortunately the alligator wins the race and you make a tasty snack.")
            else:
                print("He forgives you and gives you directions to the nearest land mass. After three days of dehydration you make it home in time for dinner.")
    else:
        print("Please enter one of the options in quotes!")
        choice()
        
choice()
        
        

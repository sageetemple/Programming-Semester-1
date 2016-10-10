import random
player = random.randint(1,6)
comp = random.randint(1,6)

dice= player>comp
if dice:
    winner="player"

if not dice:
    winner="the computer"

def rollDice():
    print("You rolled a ", player)
    print("Computer rolled a ", comp)
    print("The winner is ", winner)

rollDice()

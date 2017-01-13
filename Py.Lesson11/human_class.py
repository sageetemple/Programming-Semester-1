class Human:
    def __init__(self, h, e, s):
        self.hair = h
        self.eyes = e
        self.skin = s
        hair = h
        eyes = e
        skin = s

    def setHES(self, newH, newE, newS):
        self.hair = newH
        self.eyes = newE
        self.skin = newS

    def getHair(self):
        return self.hair
    def getEyes(self):
        return self.eyes
    def getSkin(self):
        return self.skin

def main():
    hair = input("Please enter your hair color: ")
    eyes = input("Please enter your eye color: ")
    skin = input("Please enter your skin color: ")

    human1 = Human(hair, eyes, skin)

    print("\nMy info.....\nHair: ", human1.getHair())
    print("Eyes: ", human1.getEyes())
    print("Skin: ", human1.getSkin())

    human1.setHES("brown", "brown", "brown")

    print("\nMy friend's info....\nHair: ", human1.getHair())
    print("Eyes: ", human1.getEyes())
    print("Skin: ", human1.getSkin())
main()

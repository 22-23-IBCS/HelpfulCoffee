import random


class Deck:

    def __init__(self):
        self.cards = []

class Card:

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

        def getSuit(self):
            return self.suit
        def getName(self):
            return self.name

    def main():

        print("Welcome to Black Jack!")

        a = random.randint(1,11)
        b = random.randint(1,11)
        c = random.randint(1,11)
        Num = a + b

        myList = [a, b]
        print (myList)

        Limit = 21


        for Num in Limit:

            print("want anothor one?")
            
            if input("yes"):
             print(c)
             Num = a + b + c
             print(Num)
            
            else:
                input("no")
                break

        else:

            if Num == 21:
             print("Congratulations!")
            
        
            if Num > 21:
             print("Game Over")
            
    

    if __name__ == "__main__":
        main()

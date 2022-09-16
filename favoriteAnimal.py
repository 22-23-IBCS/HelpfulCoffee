class Cat:
 
    def __init__(self, c, b, t):
        self.numLegs = 4
        self.color = c
        self.breed = b
        self.tail = t
 
 
    def getColor(self):
        return self.color
 
    def getBreed(self):
        return self.breed
 
    def getTail(self):
        return self.tail
 
    def setBreed(self, b):
        self.breed = b
 
    def setTail(self, t):
        self.tail = t
 
def main():
 
    print("This is my favorite animal and it is: ")
 
    cat1 = Cat("Black Golden", "Black Golden Shaded British Shorthair:", "Long Tail,")
    cat2 = Cat("White", "British Shorthair", "Long tail,")
    b = cat1.getBreed()
    t = cat1.getTail()
    c = cat1.getColor()
    print(b, t, c)
    cat1.setBreed("British Shorthair:")
    print(cat1.getBreed(), cat2.getTail(), cat2.getColor())
 
 
if __name__ == "__main__":
    main()
                

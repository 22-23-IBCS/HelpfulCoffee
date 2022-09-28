class Coffeeshop:
    def __init__(self):
        self.coffee = 10
        self.latte = 14
        self.chocomilk = 11
 
    def pickOption(self, myOrder):
        if myOrder == "1":
           
            return "What would you like to order?"
       
        else:
           
            return "We mix dirt in our coffee. So, what would you like to order?"
 
    def getPrice(self, coffeeOrder):
        if coffeeOrder =="1":
            return self.coffee
        if coffeeOrder =="2":
            return self.latte
        if coffeeOrder =="3":
            return self.chocomilk
        
 
    def orderOption(self, coffeeOrder):
        if coffeeOrder =="1":
            return "Gotcha 1.24 oz. hot cider\n"
        if coffeeOrder =="2":
            return "Gotcha 1.24 oz. hot cider\n"
        else:
            return "Gotcha 1.24 oz. cold cider\n"
 
 
 
 
       
 
    #def calculatePrice(self, order):
        #if order == "coffee":
            #return self.coffee
        #else:
           # return "We don't have that here"
       
 
def main():
 
    C = Coffeeshop()
    print("Hi, welcome to Charlie&Harry's cafe, please pcik an option\n")
    #need to assign a variable name to the input
    myOrder = input("1. Order\n" + "2. Learn more about the shop\n")
 
    print(str(C.pickOption(myOrder)))
   
    coffeeOrder = input("1. Coffee\n"+"2. Latte\n"+ "3. ChocolateMilk\n")
 
    print (str(C.orderOption(coffeeOrder)))
    name =  str(input(("Can I have a name for that?\n")))
 
    p = C.getPrice(coffeeOrder)
    print ("Got it. That will be $" + str(p) + "... " + str(name)+ ", here's your order. Please come again.")
   
    
    
    
 
   
 
if __name__ == "__main__":
    main()

def main():

    drink = {"Boba" : 6.69,
             "Mojito" : 10.00,
             "Orange Juice" : 3.5,
             "Coke" : 3.5,
             "Cappuccino" : 4.89,
            "Fanta": 2.5,
             "Latte": 4.0,
             "Red Bull":3.0,
             "Lemonade": 3.0,
             "Strawberry Lemonade": 3.2}

    print(list(drink.keys()))
    request = input("Which drink would you like to buy?\n")
    price = drink.get(request)
    many = int(input("How many would you want?\n"))
    print("Here you go!\nYou got " + str(many) + " " + request)
    print("That would be $" + str(round(price*many, 2)) + " dollars")



    toBuy = []
    while True:
        print(list(drink.keys()))
        res = input("What would you like to buy? Enter 'stop' if done\n")
        if res == "stop":
            break
        else:
            request1 = input("Which drink would you like to buy?\n")
            price1= (list(drink.keys()))
            many1 = int(input("How many would you want?\n"))
            price1 = drink.get(request1)
            print("Here you go!\nYou got " + str(many1) + " " + request1)
            print("That would be $" + str(round(price1*many1, 2)) + " dollars")





if __name__ == "__main__":
    main()

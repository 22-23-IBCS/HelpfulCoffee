data = {}
goals=[]

for _ in range(11):
    name = input("Enter a player's name: ")
    number = int(input("Enter the goal that this player gained: "))
    data[name] = number
    goals.append(number)

total = sum(data.values())


print("\nPercentage of each number:")

max_goal = max(goals)
player = ""

for name, number in data.items():
    if number == max_goal:
        player = name
    percentage = (number / total) * 100
    print(f"{name}: {percentage:.2f}%")
print("max goals is " + str(max_goal) + ", and it was scored by " + player)
        



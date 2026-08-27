food = ("Burger Veg","American", 45,"Small")
food1 = ("Fries","Belgium", 85,"Large with Peri Peri")
print(food) #("Burger Veg","American", 45,"Small")
print(food[0])#Burger Veg
print(food[-1])#small
all_recipes = (food, food1)
print(all_recipes[0][0])
print(all_recipes[1][2])
print(food1[1:3])
print(food[1:3])

for detail in food1:
    print(" -", detail)
for detail in food:
    print(" -", detail)    
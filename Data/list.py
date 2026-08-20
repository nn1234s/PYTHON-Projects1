#Creating aList
fruits = ["apple","mango","banana","guava","orange"]

#accessing Item by Index Start at 0
print(fruits[0])
print(fruits[-1])

#Finding total Number of item
print(len(fruits)) #Inthis case it is 5!

#Slicing - getting a range of items
print(fruits[1:4]) #In this case mango banana guava

fruits.append("orange")#addtoend
#apple mango banana guava orange

fruits.remove("mango") #removebyvalue
#apple banana guava orange

fruits.pop(1) #removebyindex
#apple guava orange

fruits.sort()#sort alphabetically
#apple guava orange

fruits.reverse()#reversethe order
#orange guava apple

fruits.clear() #removeall items
#[By code1022w]
# two related lists
roll_numbers = [1,2,3,4,5]
names = ["Code1022w","rombro2d","computer","codingal","Tech"]

# Convert to a dictionary using zip()
students = dict(zip(roll_numbers,names))
print(students)

#Look Up using rollno
print(students[1])
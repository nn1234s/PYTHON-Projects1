#creating a Dictionary
student = {"name":"Code1022w","age":13,"grade":7,"school":"KVno4"}

#Accessing values by key
print("Name",student["name"]) #Code1022w
print("age",student["age"]) #Age11

#printing the full dictionary
print("Student Information",student)
# Output will be Student Information{"name":"Code1-22w","age":11,"grade":5}

#Accessing values by key
print("Name",student["name"]) #code1022w
print("grade",student["grade"]) #grade5
print("age",student["age"]) #Age11

#SAFE ACCESS USING GET, NO ERROR IF KEY IS MISS
print(student.get("age"))
print(student.get("school","N/A"))

#Update an existing value
student["age"] = 14

# Add a new key value pair
student["school"] = "PMSHRI KENDRIYA VIDALAYA NO 4 "
print(student)
#{"name":"Code1022w","age":13,"grade":5,"school":"KVno4"}

#remove a specfic key
student.pop("grade")
print(student)
#{"name":"Code1022w","age":13,"grade":5,"school":"KVno4"}

student.clear()
print(student)
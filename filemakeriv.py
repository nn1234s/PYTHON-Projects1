file = open("science-notes.txt","w") # connect to a FiLES on the disk
file.write("Planets orbit the Sun\n,The Moon causes tides\n,Light is faster than sound\n,Planets convert sunlight to food\n") # write to file
#Old way
file = open('science-notes.txt','r')
for line in file:
    print(line.strip())
file.close()
#New way 
with open('science-notes.txt','r') as f:
    for line in f:
        print(line.strip())
#Output same both ways
# planets orbit the sun
# the moon causes tides
# light is faster than sound
# planets convert sunlight to food
file = open("maths-notes.txt","w") # connect to a FiLES on the disk
file.write("Triangles have three sides\n,Pi is 3.14\n,Area equals length times width\n,Prime numbers divide only by one\n") # write to file       
with open('maths-notes.txt','r') as f:
    for line in f:
        words = line.spilt()
        print(len(words), 'words ->', line.strip()) 
#Output
# 4 words -> triangles have three sides
# #3 words -> pi is 3.14
# 5 words -> area equals length tim        
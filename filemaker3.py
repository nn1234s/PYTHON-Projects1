file = open("class-notes.txt","w") # connect to a FiLES on the disk
file.write("Maths: Learn equations today\n,Coding: Variables and loops\n,Science: Photosynthesis\n,Coding: If statements\n,English: Essay writing\n,Coding: Functions and recursion\n,History: World war II\n") # write to file
file.close # disconnecmbt , data is sabed! 
#open files
file = open('class-notes.txt','r')
# read first 20 characters
print(file.read(20))
#close the file
file.close()
#Open the files!
file = open('class-notes.txt','r')
lines = file.readlines()
file.close()

#HOW MANY LINE ARE THERE?!?!
print('total Lines:', len(lines))
# Print each line with its number
for i in range(len(lines)):
    print(i + 1,'->',lines[i].strip())

#output
# total line 3

#open the file
file = open('class-notes.txt','r')

#Loop through every line one at a time
for line in file:
    print(line.strip())

# closing the file!
file.close()    

word = input('Skip Lines starting with:')
file = open('class-notes.txt','r')
for line in file:
    if line.startswith(word):
        print('skip ->', line.strip())
    else:
        print('keep ->',line.strip())    
file.close()        

#READ ALL LINES into a list
file = open('class-notes.txt','r')
lines = file.readlines()
file.close()

#Open a new file for wrting
out = open('odd-lines.txt','w')
#range(0 len 2) give index 0 2 4 6 everyother line
for i in range(0, len(lines),2):
    out.write(lines[i])

out.close()
print('odd lines saved to odd-lines.txt')    
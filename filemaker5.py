file = open("maths-notes.txt","w") # connect to a FiLES on the disk
file.write("Triangles have three sides\n,Pi is 3.14\n,Area equals length times width\n,Prime numbers divide only by one\n") # write to file 
file.close()      
with open('maths-notes.txt','r') as f:
    for line in f:
        words = line.split()
        print(len(words), 'words ->', line.strip()) 
import os
if os.path.exists('all-notes.txt'):
    print('all-notes.txt already exists  overwrite....')
else:
    print('all-notes.txt not found creating now....')            
file = open("all-notes.txt","w")    

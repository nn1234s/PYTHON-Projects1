
import os
if os.path.exists('all-notes.txt'):
    print('all-notes.txt already exist - Overwrite with All note')
else:
    print('Not found creating now ... all-notes.txt')    
print("Buliding single file of math and science notes")
content = ''
with open('science-notes.txt', 'r') as f:
    content += '--- science-notes.txt ---\n'
    content += f.read() + '\n'
with open('maths-notes.txt', 'r') as f:
    content += '--- maths-notes.txt ---\n'
    content += f.read() + '\n'    
with open('all-notes.txt', 'w') as out:
    out.write(content)
print('saved math & science notes to all-notes.txt!!!')  
#this file will contain both
with open('all-notes.txt','r') as f:
    for line in f:
        words = line.split()
        print(len(words), 'words ->', line.strip()) 
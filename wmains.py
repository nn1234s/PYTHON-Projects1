import os
if os.path.exists('all-notes.txt'):
    os.remove('all-notes.txt')
    print('all-notes text file was deleted')
else:
    print('file not found')    
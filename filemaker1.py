file = open("bucket-list.txt","w")

file.write("1. Get iconic Pokemon Base Set\n")
file.write("2. Get Pokemon First edition Pikachu\n")
file.write("3. Get Pokemon Korean Pack by 2026 December\n")
file.close()
print("Pokemon list saved to bucket-list.txt!")

file = open("bucket-list.txt","r")
content = file.read()
print("===My dream Pokemon collection")
print(content)
file.close()

file = open("bucket-list.txt","r")
lines = file.readlines()
file.close()
print(f"You have {len(lines)} items in your dream Pokemon collection")
print(lines)
file = open("bucket-list.txt","a")
file.write("4. Get Mewtwo card\n")
file.write("5. get Pikachu SIR\n")
file.close()
print("2 more items added!!")
file = open("bucket-list.txt", "r")
print(file.read())
file.close()




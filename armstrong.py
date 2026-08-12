# Get input from the user
num = int(input("Enter a number: "))

# Store the original number
original = num

# Count the number of digits
digits = len(str(num))

# Calculate the sum of each digit raised to the power of digit count
total = 0
while num > 0:
 digit = num % 10
 total += digit ** digits
 num = num // 10

# Check if it's an Armstrong number
if total == original:
 print(f"{original} is an Armstrong number")
else:
 print(f"{original} is not an Armstrong number")
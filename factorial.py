def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)  
num = int(input("Enter a Number!"))    
if num < 0:
    print("Nofactorial for negative number!!!")
elif num == 0:
    print("The factorial of 0 is 1")    
else:
    print("the factoriaL of ",num,"is",recur_factorial(num))    
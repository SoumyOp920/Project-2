def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
a=int(input("Enter number to find factorial: "))
b=factorial(a)
print("The factorial of",a,'is',b)
    

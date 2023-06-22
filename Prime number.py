#Check Whether a number is prime number or not Type 1 
"""
n=int(input("Enter the number other than 1 :"))
if n==2:
    print(n,"is a prime number")
else:
    flag=0
    for i in range(2,n):
        rem=n%i
        if rem==0:
            flag=1
            break
if flag==0:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")

"""
"""
#Type 1 using functions
def prime(n):
    if n==2:
        print(n,"is a prime number")
    else:
        flag=0
        for i in range(2,n):
            rem=n%i
            if rem==0:
                flag=1
                break
    if flag==0:
        print(n,"is a prime number")
    else:
        print(n,"is not a prime number")

n=int(input("Enter the number other than 1 :"))
prime(n)
"""
"""
#Type 2 block of statements that executes a task; when called by a function it returnes the value to the calling function.
n=int(input("Enter the number:"))
if n>1:
    for i in range(2,(n+1)//2):
        if n%i==0:
            print(n,"is not a prime number.")
            break
        else:
            print(n,"is a prime number")
else:
    print(n,"is not a prime number.")

#Type 2 using function
def prime(n):
    if n==2:
        print(n,"is a prime number")
    else:
        flag=0
        for i in range(2,(n+1)//2):
            rem=n%i
            if rem==0:
                flag=1
    return flag

n=int(input("Enter the number other than 1 :"))
prime(n)
f=prime(n)
if f==0:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
    

#Program to print the prime numbers from 1 to 100
def prime(num1,num2):
    for i in range(num1,num2):
        prime=True
        for j in range(2,i):
            if(i%j==0):
                prime=False
        if prime==True:
            print(i,"is a prime number.")

n1=int(input("Enter the starting number:"))
n2=int(input("Enter the ending number:"))
f1=prime(n1,n2)

"""

    






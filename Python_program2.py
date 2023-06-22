'''
#Program to find the sum of the series 1+2+3+...N
N=int(input("Enter the number of terms:"))
su=0
for i in range(1,N+1):
    su+=i
print(su)
'''
'''
#Program to find the sum of the series 1/1+1/2+1/3+..
n=int(input("Enter the number of terms:"))
tot=0
for i in range(1,n+1):
    tot+=1/i
print(tot)
'''

'''
#Program to find the sum of the series 1+3+5..N
n=int(input("Enter the number of terms:"))
tot=0
for i in range(1,n+1,2):
    tot=tot+i
    print(i,end=" ")
print('\n' "The sum of the series is ",tot)
'''
'''
n=int(input("Enter the number of terms:"))
tot=0
for i in range(1,n+1,2):
    tot=tot+ 1/i
print(tot)
'''
'''
n=int(input("Enter the number of terms:"))
tot=0
for i in range(2,n+2,2):
    tot+=i
print(tot)
'''
'''
#Program to find sum of series 1/2+2/3+3/4...(n-1)/n
n=int(input("Enter the number of sterms:"))
tot=0
for i in range(1,n):
    tot+=i/(i+1)
print(tot)
'''
'''
#program to find the sum of series 5^2+10^2+15^2+...N^2
n=int(input("Enter the number of terms:"))
tot=0
for i in range(5,(5*n)+1,5):
    tot+=i*i
print(tot)
'''
'''
#program to find the sum of squares of the series 1^2+2^2+3^2+...N^2
n=int(input("Enter the number of series:"))
tot=0
for i in range(1,n+1):
    tot=tot+(i*i)
print(tot)
'''
'''
#Program to find the sum of cubes of the series 1^3+2^3+3^3+...n^3
n=int(input("Enter the number of series:"))
tot=0
for i in range(1,n+1):
    tot=tot+(i**3)
print(tot)
'''
'''
.Write a program to find the sum of series 1^1/1+2^2/2+3^3/3...+nn/n
n=int(input("Enter the number of terms:"))
tot=0
for i in range(1,n+1):
    tot+=(i*i)/i
print(tot)
'''
'''
#Write a program to find the sum of series 1+4-9+16-25+.....+N
import math
n=int(input("Enter the last term N as perfect square in the series:"))
#Squares of natural numbers
tot=1
print(1,end="")
sign=1
temp=int(math.sqrt(n))
for i in range(2,temp+1):
    print(sign*(i*i),end=" ")
    tot=tot+sign*(i*i)
    sign=sign*(-1)
print(tot,end=' ')
'''
'''
n=int(input("Enter the last term N as perfect square in the series:"))
#Squares of natural numbers
tot=1
print(1,end="")
sign=1
for i in range(2,n+1):
    print(sign*(i*i),end=" ")
    tot=tot+sign*(i*i)
    sign=sign*(-1)
print(tot,end=' ')
'''
'''
#Program to find the sum of the series 1-2+3-4+...
n=int(input("Enter the number of terms:"))
tot=0
sign=1
for i in range(1,n+1):
    tot=tot+sign*i
    sign=sign*(-1)
print(tot)
'''
#Program to find the sum of the series 1/2-2/3+3/4-4/5+....N/N+1
n=int(input("Enter the number of terms:"))
tot=0
sign=1
for i in range(1,n+1):
    tot=tot+(sign)*(i/i+1)
    sign=sign*(-1)
    
print(tot)

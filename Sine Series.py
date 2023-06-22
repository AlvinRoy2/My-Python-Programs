#Program to print the sine series
n=int(input("Enter the limit:"))
x=int(input("Enter the value in degree:"))
#Converting to Radians
x=x*(3.14/180)
#Initialize Power,Factorial to be 1
P=1
f=1
#Initialize the sum to be the r since it adds up the first value and sign to be -1
sum1=x
sign=-1
#The Factorial and the power both are odd and starts from 3 uptill n+1 in steps of two
for i in range(3,n+1,2):
    x=x*sign
    #Using the built in function pow to calculate power the degree raised to the power of i
    p=pow(x,i)
    #It will multiply 3 by itself and then when 5 comes it will store the value of f as 6 and multiply 4 and #5 to it and f's value will get updated.
    f=f*i*(i-1)
    sum1=sum1+P/f
print(sum1)

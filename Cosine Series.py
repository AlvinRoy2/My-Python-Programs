#Program to print the Cosine series
n=int(input("Enter the limit:"))
x=int(input("Enter the value in degree:"))
#Converting to Radians
x=x*3.14/180
print(x)
#Initialize Power,Factorial to be 1
P=1
f=1
#Initialize the sum to be the r since it adds up the first value and sign to be -1
sum1=1
sign=1
for i in range(2,n+1,2):
    #Since We are already printing 1 just change the sign to -1 and then add
    sign=sign*-1
    #Using the built in function pow to calculate power the degree raised to the power of i
    P=pow(x,i)
    #It will multiply 2 by itself and then when 4 comes it will store the value of f as 2 and multiply 3 to it #and f's value will get updated.
    f=f*i*(i-1)
    sum1=sum1+sign*P/f
print(sum1)

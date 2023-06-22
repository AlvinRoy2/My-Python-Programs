# Simple Interest
prin=int(input("Enter the principal amount:"))
rate=int(input("Enter the rate of the interest:"))
no1=int(input("Enter the number of years:"))
SI=(prin*rate*no1)/100
print("The simple interest is",SI)


# Compound Interest
prin=int(input("Enter the principal amount:"))
rate=int(input("Enter the rate of the interest:"))
No_of_years=int(input("Enter the number of years:"))
rtemp=rate/100
temp1=prin*(1+rtemp)
amt=(temp1)**No_of_years
print("The amt is:",amt)
CI=amt-prin
print("The compound interest is:",CI)

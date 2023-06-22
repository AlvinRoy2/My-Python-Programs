#Program to print heart shape
rows=int(input("Enter the number of rows:"))
col=int(input("Enter the number of columns:"))
for i in range(rows):
    for j in range(col):
        if(i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
            print("*",end="   ")
        else:
            print(end="   ")
    print()


rows=int(input("Enter the number of rows:"))
col=int(input("Enter the number of columns:"))
for i in range(1,rows+1):
    for j in range(1,col+1):
        if (j-i==2 or i+j==8 or i==3):
            print("*  ",end="")
        else:
            print("   ",end="")
    print()

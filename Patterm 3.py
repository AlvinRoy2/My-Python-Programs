rows=int(input("Enter the number of rows:"))
#i represent rows
#j represents no: of columns
#Rows is the no: of rows
for i in range(1,6):
    for j in range(i,rows+1):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print(" ")

#05 Triangle of stars
rows=int(input("Enter the number of rows:"))
for i in range(1, rows+1):
    for j in range(i,rows+1):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    for l in range(i-1,0,-1):
        print("*",end=" ")
    print()

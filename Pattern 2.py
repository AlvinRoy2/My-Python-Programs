#03
rows=int(input("Enter the number of rows:"))
for i in range(1,rows+1):
    for j in range(i,rows+1):
        print("*",end="")
    print('')


#04
rows=int(input("Enter the number of rows:"))
for i in range(1,rows):
    for k in range(rows,i,-1):
        print(" ",end=' ')
    for j in range(1,i+1):
        print("*",end=' ')
    print()
    

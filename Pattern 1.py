#01
rows=int(input("Enter the number of rows:"))

for i in range(1,rows+1):
    for j in range(1,rows+1):
        print("*",end="")
    print('')

#02
rows=int(input("Enter the number of rows:"))

for i in range(1,rows+1):
    for j in range(i):
        print("*",end="")
    print('')
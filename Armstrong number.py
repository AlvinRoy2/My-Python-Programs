n1=int(input("Enter the starting number:"))
n2=int(input("Enter the ending number:"))

for i in range(n1,n2+1):
    temp=len(str(i))
    su=0
    temp1=i
    while temp1>0:
        digit=temp1%10
        su=su + digit**temp
        temp1//=10
    if i==su:
        print(i,"is an Armstrong number")

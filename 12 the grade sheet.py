# 12 th Grade sheet
print("12th Grade Sheet")
sch=input("Enter the school name:")
reg=int(input("Enter the register number:"))
ses=input("Enter the session of the exam:")
name=input("Enter the name of the student:")
lan=int(input("Enter the marks in language:"))
eng=int(input("Enter the marks in english:"))
mat=int(input("Enter the marks in maths:"))
phy=int(input("Enter the marks in physics:"))
che=int(input("Enter the marks in Chemistry:"))
comp=int(input("Enter the marks in computer science:"))
tot=lan+eng+mat+che+phy+comp
avg=tot/6
print("The total mark: ",tot)
print("The average mark: ",avg)
print("Thank you")

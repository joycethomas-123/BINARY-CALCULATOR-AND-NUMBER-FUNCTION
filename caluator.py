x=input("enter the first no: ")
y=input("enter the second no: ")
f=str(input("which operation? +,-,/,* : "))
if f=="+":
    addition=float(x)+float(y)
    print(addition)
elif f=="-":
    subraction=float(x)-float(y)
    print(subraction)
elif f=="*":
    multiplication=float(x)*float(y)
    print(multiplication)
elif f=="/":
    division=float(x)/float(y)
    if y!=0:
        print(division)
    else:
        print("cannot be determined")
else:
    print("invalid input")

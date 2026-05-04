n=int(input("enter a number:"))
if n>0:
    print("number is positive")
elif n<0:
    print("number is negative")
else:
    print("number is zero")
[25bcs142@mepcolinux ex1]$cat pattern.py
n=int(input("enter number:"))
if n<=0:
    print("invalid input")
else:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print( )

a=float(input("enter employee's monthly salary:"))
b=int(input("no of days leave taken:"))
if b==2:
    print("no deduction is salary:")
    print("employee's salary is:",a)
elif b>2:
    c=(b-2)*200
    print("the deduction amount is",c)
    print("final salary of employee is",a-c)
else:
   print("invalid choice")

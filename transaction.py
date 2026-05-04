a=float(input("enter your account balance:"))
print("your initial account balance is:")
print("mode of transaction")
print("1.deposit")
print("2.withdraw")
b=int(input("enter your choice:"))
c=float(input("enter your transaction:"))
if b==1:
    print("amount deposited successfully")
    print("your account balance is:",a+c)
elif b==2:
    print("amount withdrawed successfully")
    print("your account balance is:",a-c)
else:
    print("invalid choice")

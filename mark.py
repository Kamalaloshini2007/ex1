m1=int(input("enter 1st subject mark:"))
m2=int(input("enter 2nd subject mark:"))
m3=int(input("enter 3rd subject mark:"))
m4=int(input("enter 4th subject mark:"))
m5=int(input("enter 5th subject mark:"))
total=m1+m2+m3+m4+m5
print("the total mark is:",total)
percentage=total/5
print("the percentage is:",percentage)
if percentage>=90:
    print("grade O")
elif percentage>=80:
    print("grade A+")
elif percentage>=70:
    print("grade A")
elif percentage>=60:
    print("grade B+")
elif percentage>=55:
    print("grade B")
else:
    print("grade C")

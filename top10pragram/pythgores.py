a,b,c =5,3,4
if a<b:
    temp=a
    a=b
    b=temp
elif a<c:
    temp=a
    a=c
    a=temp
if a*a==b*b+c*c:
    print("hence given number is pythagoras number")
else:
    print("given number is not pyhthagoras theorem")
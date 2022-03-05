n=int(input("enter any digit"))
while n!=0:
    r=n%10
    n=n//10
    print(r,end="")
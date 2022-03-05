total=int(input("enter total number to check prime or not"))
while total!=0:
    total-=1
    n=int(input("enter number"))
    isprime=True
    div=2
    while div*div<n:
        if n%div==0:
            isprime=False
            break
        div+=1
    if isprime:
        print("prime")
    else:
        print(not print)

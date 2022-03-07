t=int(input())
while t!=0:
    t-=1
    isprime=True
    div=2
    n=int(input())
    while div * div <=n:
        if n%div==0:
            isprime = False
            break
        div+=1
    if isprime:
        print("prime")
    else:
        print("not prime")
    # print("prime")if isprime else print("not prime")
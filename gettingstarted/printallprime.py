low=int(input())
high=int(input())
for n in range(low,high+1):
    div=2
    isprime=True
    while div*div <=n:
        if n%div==0:
            isprime=False
            break
        div+=1
    if isprime:
        print(n)
n=10
for i in range(n+1):
    isprime=True
    div=2
    while div*div<=i:
        if i%div==0:
            isprime=False
        div+=1
    if isprime:
        print(i)
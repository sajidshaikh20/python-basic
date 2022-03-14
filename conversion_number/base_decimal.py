n=int(input())
b=6
conv=0
pow=0
while n!=0:
    r=n%10
    conv+=r*b**pow
    pow+=1
    n//=10
print(conv)
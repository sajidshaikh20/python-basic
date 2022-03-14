n=int(input())
conv=0
base=8
pow=0
while n!=0:
    rem=n%base
    conv=conv+rem*10**pow
    pow+=1
    n//=base
print(conv)
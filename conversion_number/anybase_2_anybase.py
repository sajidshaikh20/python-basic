n=int(input())
base1=6
base6=0
temp=n
pow=0
# first decimal to convert base becaunse in computer every number is decimal number
while temp!=0:
    rem=temp%10
    base6=base6+rem*6**pow
    pow+=1
    temp//=10
print(base6)
# now convert base 6 to base 3
pow=0
base3=0
while base6!=0:
    rem=base6%6
    base3=base3+rem*3**pow
    pow+=1
    base6//=10
print(base3)
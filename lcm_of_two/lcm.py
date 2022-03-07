num1=12
num2=24
div=2
lcm=1
while num1!=1 and num2!=1:
    if num1%div==0 or num2%div==0:
        lcm=lcm*div
    if num1%div==0:
        num1=num1//div
    if num2%div==0:
        num2=num2//div
    else:
        div+=1
print(lcm)

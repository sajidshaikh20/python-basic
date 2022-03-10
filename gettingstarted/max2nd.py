arr=[2,5,7,-1,42,31]
max1=arr[0]
max2=arr[1]
for value in arr :
    if max1<value:
        temp=max1
        max1=value
        max2=temp
print(max2)
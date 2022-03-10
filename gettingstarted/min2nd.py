arr=[2,5,7,12,1,-1,42,31]
min1=arr[0]
min2=arr[1]
for value in arr :
    if value<min1:
        temp=min1
        min1=value
        min2=temp
print(min2)
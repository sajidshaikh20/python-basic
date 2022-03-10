arr=[2,5,7,545641,4222,3114]
max1=arr[0]
max2=arr[1]
n =len(arr)
for i in range(2,n):
    if arr[i]>max1:
        max2=max1
        max1=arr[i]
    elif arr[i]>max2:
        max1!=arr[i]
        max2=arr[i]
print(max2)

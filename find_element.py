# n=int(input())
list = [2,5,6,7,8,9]
d =2
isavail=False
for i in range(0,len(list)):
    # print(list)
    if i==d:
        isavail=True
        break
if isavail:
    print("find")
else:
    print("notfound")
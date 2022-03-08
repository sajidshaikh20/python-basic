def main():
    # input
    arr = input().split(" ")
    a = int(arr[0])
    b= int(arr[1])
    c=int(arr[2])
    if a<b:
        temp=a
        a=b
        b=temp
    if a<c:
        temp=a
        a=c
        c=temp
    if a*a==b*b+c*c:
        print("true")
    else:
        print("false")
    try:
        b = int(arr[1])
        c = int(arr[2])
    except:
        b = int(input())
        c = int(input())
    

if __name__ == "__main__":
    main()
    
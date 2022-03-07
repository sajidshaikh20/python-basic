def rotate(n,k):
    # write your code here
    digit=-1
    temp=n
    while temp!=0:
        temp=temp//10
        digit+=1
    num=10**(digit)
    # print(num*4)
    k=k%num
    while k!=0:
        rem=n%10
        ans=rem*num
        n=n//10
        n=ans+n
        k-=1
    print(n)
def main():
    n = int(input())
    k = int(input())
    rotate(n,k)

if __name__=="__main__":
    main()
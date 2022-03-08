def primeFac(n):
    # write your code here
    div=2
    while n!=1:
        if n%div==0:
            n=n//div
            print(div,end=" ")
        if n%div!=0:
            div+=1
def main():
    n = int(input())
    primeFac(n)

if __name__=="__main__":
    main()
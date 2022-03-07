def reverse(n):
    # write your code here
    while n!=0:
        r=n%10
        print(r)
        n=n//10

def main():
    n = int(input())
    reverse(n)

if __name__=="__main__":
    main()
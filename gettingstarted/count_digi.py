def count(n):
    # write your code here
    temp=0
    while n!=0:
        n=n//10
        temp+=1
    print(temp)

def main():
    n = int(input())
    count(n)

if __name__=="__main__":
    main()
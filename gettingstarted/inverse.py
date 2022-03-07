def inverse(n):
    # write your code here
    inverse=0
    value=0
    while n!=0:
        value+=1
        ind=n%10
        inverse=inverse+value*10**(ind-1)
        n=n//10
    print(inverse)
def main():
    n = int(input())
    inverse(n)

if __name__=="__main__":
    main()
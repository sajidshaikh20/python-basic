def digits(n):
    # write your code here
    power=-1
    n1=n
    while n1!=0:
        n1=n1//10
        power+=1
    div=pow(10,power)
   
    while div!=0:
        q=n//div
        print(q)
        rem=n%div
        n=rem
        div=div//10
        
             
def main():
    n = int(input())
    digits(n)

if __name__=="__main__":
    main()
def gcdandlcm(n1,n2):
# code of gcd
    a=n1
    b=n2
    while(n1%n2!=0):
        rem=n1%n2
        n1=n2
        n2=rem
    gcd=n2
    
    # code for lcm
    lcm=(a*b)//gcd
    print(gcd)
    print(lcm)
            
def main():
    n1 = int(input())
    n2 = int(input())
    gcdandlcm(n1,n2)

if __name__=="__main__":
    main()
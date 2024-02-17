n,m=tuple(map(int,input().split()))

def find_gcd(n,m):
    gcd=0
    for i in range(max(n,m),n*m+1):
        if i%n==0 and i%m==0:
            gcd=i
            break
    print(gcd)        

find_gcd(n,m)
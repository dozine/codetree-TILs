x,y=tuple(map(int,input().split()))

def digit_sum(n):
    digitsum=0
    while n>0:
        digitsum+=(n%10)
        n//=10
    return digitsum

ans=0
for i in range(x,y+1):
    ans=max(ans,digit_sum(i))
print(ans)
N = int(input())

# Write your code here!

memo = [-1]*(N+1)

def fibbo(n):
    if memo[n] != -1:
        return memo[n]
    if n<=2:
        memo[n]=1
    else:
        memo[n]=fibbo(n-1)+fibbo(n-2)
    return memo[n]

ans = fibbo(N)
print(ans)
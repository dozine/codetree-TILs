N = int(input())

# Write your code here!
def fibbo(n):
    if n<=2:
        return 1
    else: 
        return fibbo(n-1)+fibbo(n-2)

ans= fibbo(N)
print(ans)
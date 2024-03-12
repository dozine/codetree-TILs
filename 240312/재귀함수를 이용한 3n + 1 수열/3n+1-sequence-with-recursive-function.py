n=int(input())
def f(a):
    if a==1:
        return 0
    if a%2==0:
        return f(a//2)+1
    else:
        return f(3*a+1)+1

print(f(n))
a,b,c=tuple(map(int,input().split()))

def f(n):
    if n<10:
        return n
    return f(n//10)+n%10

print(f(a*b*c))
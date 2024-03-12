n=int(input())

def f(a):
    if a==1:
        return 1
    if a==2:
        return 2
    return f(a//3)+f(a-1)

print(f(n))
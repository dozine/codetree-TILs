n=int(input())

def f(a):
    if a==1:
        return 2
    if a==2:
        return 4
    return f(a-2)*f(a-1)%100

print(f(n))
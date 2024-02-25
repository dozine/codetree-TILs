a,b=map(int,input().split())

def function(a,b):
    if (a>b):
        b*=2
        a+=25
    else:
        a*=2
        b+=25
    return a,b

a,b=function(a,b)

print(a,b)
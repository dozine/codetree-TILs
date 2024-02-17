n=int(input())

def function(n):
    if n%2==0:
        if ((n//10)+(n%10))%5==0:
            print("Yes")
    else:
        print("No")

function(n)
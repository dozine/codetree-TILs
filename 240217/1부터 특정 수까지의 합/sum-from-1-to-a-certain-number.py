N=int(input())

def function(N):
    sum=0
    for i in range(1,N+1):
        sum+=i
    print(sum//10)

function(N)
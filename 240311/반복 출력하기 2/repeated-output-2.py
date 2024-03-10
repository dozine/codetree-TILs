N=int(input())
def function(n):
    if n==0:
        return
    function(n-1)
    print("HelloWorld")

function(N)
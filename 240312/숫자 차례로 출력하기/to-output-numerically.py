n=int(input())

def function(n):
    if n ==0:
        return 
    function(n-1)
    print(n,end=" ")

def function2(n):
    if n==0:
        return 
    print(n,end=" ")
    function2(n-1)

function(n)
print()
function2(n)
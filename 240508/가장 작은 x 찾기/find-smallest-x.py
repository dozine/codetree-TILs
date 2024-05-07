import sys
MAX_NUM=10000
n = int(input())
arr=[
    tuple(map(int,input().split()))
    for _ in range(n)
]

def satisfied(x):
    for a,b in arr:
        x*=2
        if x<a or x>b:
            return False
    return True


for x in range(1,MAX_NUM+1):
    if satisfied(x):
        print(x)
        break
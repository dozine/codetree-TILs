# dictionary에서 반복문을 사용할 때, 값에 대해서만 반복하려면 dict.value()를 사용하고 
# 키와 값 둘다에 대해서 반복하려면 dict.items()를 사용하면 된다.
from sortedcontainers import SortedDict

n=int(input())
d=SortedDict()

for _ in range(n):
    command=list(input().split())
    if command[0]=="add":
        k=int(command[1])
        v=int(command[2])
        d[k]=v
    elif command[0]=="remove":
        k=int(command[1])
        d.pop(k)
    elif command[0]=="find":
        k=int(command[1])
        if k not in d:
            print("None")
        else:
            print(d[k])
    else: 
        if not d:
            print("None")
        else:
            for value in d.values():
                print(value,end=" ")
            print()
        
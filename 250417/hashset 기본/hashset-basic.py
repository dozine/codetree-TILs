n = int(input())

# Please write your code here.
s=set()

for _ in range(n):
    command=list(input().split())
    if command[0]=="add":
        val=command[1]
        s.add(val)
    elif command[0]=="remove":
        val=command[1]
        s.remove(val)
    else:
        val=command[1]
        if val not in s:
            print("false")
        else:
            print("true")

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# Please write your code here.
b=set(b)

for i in b:
    if i in a:
        print(1)
    else:
        print(0)

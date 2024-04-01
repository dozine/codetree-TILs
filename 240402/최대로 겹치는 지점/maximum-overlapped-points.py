n =int(input())
segments=[
    tuple(map(int,input().split()))
    for _ in range(n)
]

blocks=[0]*(101)
for a,b in segments:
    for i in range(a,b+1):
        blocks[i] +=1
max_num=max(blocks)
print(max_num)
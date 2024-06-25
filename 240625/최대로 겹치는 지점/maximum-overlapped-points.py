n=int(input())
segments=[
    tuple(map(int,input().split()))
    for _ in range(n)
]
offset=100
blocks=[0]*200

for x1,x2 in segments:
    x1,x2=x1+offset,x2+offset
    for i in range(x1,x2+1):
        blocks[i]+=1

max_block=max(blocks)
print(max_block)
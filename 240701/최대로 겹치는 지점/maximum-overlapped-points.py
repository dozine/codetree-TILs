n=int(input())
segments=[
    tuple(map(int,input().split()))
    for _ in range(n)
]
blocks=[0]*200

for x1,x2 in segments:
    for i in range(x1,x2+1):
        blocks[i]+=1

max_block=max(blocks)
print(max_block)
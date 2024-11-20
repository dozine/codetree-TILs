n=int(input())

block=[
    int(input())
    for _ in range(n)
]

def remove_block(arr,start,end):
    return arr[:start-1] + arr[end:]

s1,e1=tuple(map(int,input().split()))
new_block=remove_block(block,s1,e1)

s2,e2=tuple(map(int,input().split()))
result_block=remove_block(new_block,s2,e2)


print(len(result_block))
for i in result_block:
    print(i)

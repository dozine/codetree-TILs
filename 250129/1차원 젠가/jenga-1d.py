n = int(input()) 
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split()) 

remaining_blocks = blocks[1:s1] + blocks[e1:]

remaining_blocks = remaining_blocks[1:s2] + remaining_blocks[e2:]


print(len(remaining_blocks))
for i in remaining_blocks:
    print(i)


# n=int(input())
# string=input()

# cnt=0
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if string[i]=='C' and string[j]=='O' and string[k]=='W':
#                 cnt+=1

# print(cnt)


n = int(input())
s = input()

c = 0
co = 0
cow = 0

for char in s:
    if char == 'C':
        c += 1
    elif char == 'O':
        co += c
    elif char == 'W':
        cow += co

print(cow)
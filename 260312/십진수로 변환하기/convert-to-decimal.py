binary = list(map(int,input().split()))
length = len(binary)

num = 0
for i in range(length):
    num = num * 2 + binary[i]

print(num)
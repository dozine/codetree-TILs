n=int(input())
words=[
    input()
    for _ in range(n)
]
words.sort()
for i in words:
    print(i)
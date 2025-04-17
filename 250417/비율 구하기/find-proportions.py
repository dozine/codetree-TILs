from sortedcontainers import SortedDict

n = int(input())
words = [input() for _ in range(n)]
freq=SortedDict()

# Please write your code here.
for word in words:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1

for word, cnt in freq.items():
    ratio=cnt/n*100
    print(f"{word} {ratio:.4f}")
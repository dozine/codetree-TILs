n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
freq=dict()
ans=0
for word in words:
    if word not in freq:
        freq[word]=1
    else:
        freq[word]+=1
    
    ans=max(ans,freq[word])
print(ans)
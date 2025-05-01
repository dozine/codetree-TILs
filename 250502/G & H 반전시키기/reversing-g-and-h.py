n = int(input())
a = input()
b = input()

# Please write your code here.
ans = 0
mismatched=False
for i in range(n):
    if a[i] !=b[i]:
        if not mismatched:
            mismatched=True
            ans+=1
    else:
        mismatched=False

print(ans)
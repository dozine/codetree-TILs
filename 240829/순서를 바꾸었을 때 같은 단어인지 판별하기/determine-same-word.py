f_word=input()
s_word=input()

f_word=list(f_word)
s_word=list(s_word)
f_word.sort()
s_word.sort()
cnt=0
for i in range(len(f_word)):
    if f_word[i]==s_word[i]:
        cnt+=1
if cnt==len(f_word):
    print("Yes")
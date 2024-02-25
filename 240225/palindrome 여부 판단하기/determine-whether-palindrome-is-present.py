_str=list(map(str,input().split()))

def palindrome(a):
    for i in range(len(a)):
        if a[i]==a[len(a) - i -1]:
            return True 
    return False

if palindrome(_str):
    print("Yes")
else:
    print("No")
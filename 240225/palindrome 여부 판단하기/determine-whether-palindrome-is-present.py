_str= input()

def palindrome(a):
    for i in range(len(a)):
        if a[i]!=a[len(a) - i -1]:
            return False 
    return True

if palindrome(_str):
    print("Yes")
else:
    print("No")
A=input()

def function(n):
    leng=len(n)
    for i in range(leng):
        if n[i]!=n[0]:
            return True
    return False

if function(A):
    print("Yes")
else:
    print("No")
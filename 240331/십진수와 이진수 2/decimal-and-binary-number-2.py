n=list(map(int,list(input())))
length=len(n)
num=0
for i in range(length):
    num=num*2+n[i]
num*=17
digits=[]
while True:
    if num<2:
        digits.append(num)
        break
    digits.append(num%2)
    num//=2
for digit in digits[::-1]:
    print(digit,end="")
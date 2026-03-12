n = int(input())

# Please write your code here.

# def is_binary(n):
#     if n<2 : 
#         return False
#     for i in range(int(n**0.5)+1):
#         for j in range(i):
#             if i%j==0:
#                 return False
digits = []
while True:
    if n < 2:
        digits.append(n)
        break
    digits.append(n % 2)
    n //= 2
    
for digit in digits[::-1]:
    print(digit, end="")
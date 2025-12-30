def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
A = int(input())
B = int(input())
C = int(input())
D = int(input())
num = A * D - B * C
den = B * D
g = gcd(num, den)
num //= g
den //= g
print(num, "/", den)

# 2)
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
A = int(input())
B = int(input())
g = gcd(A, B)
lcm = (A * B) // g
print("GCD =", g)
print("LCM =", lcm)

# 2)
import math
def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
diag = float(input("Diagonal: "))
area1 = triangle_area(a, b, diag)
area2 = triangle_area(c, d, diag)
total_area = area1 + area2
print("Area =", total_area)

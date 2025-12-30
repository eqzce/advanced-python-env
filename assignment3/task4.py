def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
A = int(input())
B = int(input())
C = int(input())
D = int(input())
num = A * D
den = B * C
g = gcd(num, den)
num //= g
den //= g
print(num, "/", den)

# 2)
a = float(input("Center x (a): "))
b = float(input("Center y (b): "))
r = float(input("Radius: "))
points = []
for i in range(3):
    x = float(input(f"{i+1} x: "))
    y = float(input(f"{i+1} y: "))
    points.append((x, y))
count = 0
for x, y in points:
    if (x - a)**2 + (y - b)**2 < r**2:
        count += 1
print("Inside the circle: ", count)

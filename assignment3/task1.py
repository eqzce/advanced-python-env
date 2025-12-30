import math
print("Choose shape (square, rectangle, triangle, circle): ")
choice = input("Enter your choice: ")
if choice == "square":
    a = float(input("Enter a: "))
    area = a**2
    print("Area = ", area)
elif choice == "rectangle":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    area = a * b
    print("Area = ", area)
elif choice == "triangle":
    b = float(input("Enter b: "))
    h = float(input("Enter h: "))
    area = 0.5 * b * h
    print("Area = ", area)
elif choice == "circle":
    r = float(input("Enter r: "))
    area = math.pi * r * r
    print("Area = ", area)
else:
    print("Wrong choice")

# 2)

arrays = []
for i in range(3): 
    arr = list(map(int, input().split()))
    arrays.append(arr)
for i in range(3):
    arr = arrays[i]
    s = sum(arr)
    mean = s / len(arr)
    print("Sum =", s)
    print("Arithmetic mean =", mean)

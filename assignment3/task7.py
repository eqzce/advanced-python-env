def right_triangle_area(a, b):
    return 0.5 * a * b
def rectangle_area(a, b):
    return a * b
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
t = float(input("t = "))
triangle_part = right_triangle_area(x, y)
rectangle_part = rectangle_area(z, t)
total_area = triangle_part + rectangle_part
print("Area =", total_area)

# 2)
num = int(input("Enter integer: "))
octal_code = format(num, '010o')
print(octal_code)

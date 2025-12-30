import math
a = float(input("Side of hexagon: "))
area = (math.sqrt(3) / 4) * a * a
print("Area = ", area)

# 2)
areas = []
for i in range(1, 4):
    print(i,":")
    a = float(input("First side: "))
    b = float(input("Second side: "))
    area = a * b
    areas.append(area)
lenght = len(areas)
for i in range(lenght):
    print(f"Area {i+1} = ", areas[i])

import math
def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)
print("Triangle 1")
a1 = float(input("First leg: "))
b1 = float(input("Second leg: "))
print("Triangle 2")
a2 = float(input("First leg: "))
b2 = float(input("Second leg: "))
h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)
print("Hypotenuse 1 =", h1)
print("Hypotenuse 2 =", h2)
if h1 > h2:
    print("Triangle 1 greater")
elif h2 > h1:
    print("Triangle 2 greater")
else:
    print("Triangles equal")

# 2)
text = input("Enter a string: ")
words = text.split()
sorted = []
for word in words:
    sorted_word = "".join(sorted(word))
    sorted.append(sorted_word)
result = " ".join(sorted)
print(result)

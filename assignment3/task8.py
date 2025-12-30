n = int(input("Enter n: "))
for num in range(1, n + 1):
    divisible = True
    for digit in str(num):
        if digit == '0' or num % int(digit) != 0:
            divisible = False
            break
    if divisible:
        print(num, end=" ")

# 2)
def swap_first_last(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
m = int(input())
A = []
for i in range(m):
    A.append(int(input()))
print("Original array:", A)
swap_first_last(A)
print("Array after swapping: ", A)

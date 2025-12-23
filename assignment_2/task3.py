problem = input("Enter your problem: ")
if "+" in problem:
    op = "+"
    a, rest = problem.split("+", 1)
elif "-" in problem:
    op = "-"
    a, rest = problem.split("-", 1)
else:
    print("operation is wrong")
    exit()
b, res = rest.split("=")
if a.isalpha():
    var = a
    num = int(b)
    res = int(res)
    if op == "+":
        ans = res - num
    else:
        ans = res + num
else:
    var = b
    num = int(a)
    res = int(res)
    if op == "+":
        ans = res - num
    else:
        ans = num - res
print(ans)

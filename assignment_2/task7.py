n = int(input())
lines = []
for i in range(n):
    s = input()
    lines.append(s)
max_len = max(len(s) for s in lines)
result = [s + "_" * (max_len - len(s)) for s in lines]
for s in result:
    print(s)

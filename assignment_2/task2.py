str = input()
cycle = input()
n = len(cycle)
count = 0
for i in range(len(str) - n + 1):
    if str[i:i+n] in cycle + cycle:
        count+=1
print(count)

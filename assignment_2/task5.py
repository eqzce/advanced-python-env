letters = set("ABCEHKMOPTXY")
n = int(input())
for _ in range(n):
    lic = input().strip()
    if len(lic) != 6:
        print("No")
    if(lic[0] in letters and
       lic[1].isdigit() and
       lic[2].isdigit() and
       lic[3].isdigit() and
       lic[4] in letters and
       lic[5] in letters):
        print("Yes")
    else:
        print("No")

a = float(input("Enter a number: "))
int_part = int(a)
frac_part = round((a-int_part)*100)
ans = frac_part + int_part/100
print(ans)

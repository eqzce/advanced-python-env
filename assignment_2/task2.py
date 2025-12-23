import re
text = input("Type string: ")
pattern1 = ">>-->"
pattern2 = "<--<<"
count1 = len(re.findall(f"(?={pattern1})", text))
count2 = len(re.findall(f"(?={pattern2})", text))
ans = count1+count2
print(ans)

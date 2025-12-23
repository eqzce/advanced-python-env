text = input("Type string: ")
pattern1 = ">>-->"
pattern2 = "<--<<"
count1 = text.count(pattern1)
count2 = text.count(pattern2)
ans = count1 + count2
print(ans)

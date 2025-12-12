s1, s2, s3 = input("Enter salaries of 3 employees: ").split()
maxsal = max(int(s1),int(s2),int(s3))
minsal = min(int(s1),int(s2),int(s3))
print(maxsal-minsal)

# or

s1, s2, s3 = map(int, input("Enter salaries of 3 employees: ").split())
maxsal = max(s1,s2,s3)
minsal = min(s1,s2,s3)
print(maxsal-minsal)

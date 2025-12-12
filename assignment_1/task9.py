ticket = input("Enter your ticket number: ")
if sum(map(int, ticket[:3]))==sum(map(int, ticket[3:])):
    print("YES")
else:
    print("NO")

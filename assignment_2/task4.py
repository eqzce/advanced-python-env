n, m = map(int, input().split())
text = input()
unique_words = set()
for i in range(n - m + 1):
    word = text[i:i+m]
    unique_words.add(word)
print(len(unique_words))

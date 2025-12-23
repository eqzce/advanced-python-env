prod = input("Enter products: ").split()
prod_uniq = set(prod)
n = len(prod)
n_uniq = len(prod_uniq)
freq = {}
for item in prod_uniq:
    freq[item] = prod.count(item)
print("Purchase frequency:")
for item, count in freq.items():
    print(f"{item}: {count}")
max_count = max(freq.values())
most_popular = None
for item, count in freq.items():
    if count == max_count:
        most_popular = item
        break
print("Most populat item: ", most_popular)
purchased_once = []
for item, count in freq.items():
    if count == 1:
        purchased_once.append(item)
print("Purchasaed once: ", " ".join(purchased_once))
items_list = list(freq.items())
for i in range(len(items_list)):
    for j in range(i + 1, len(items_list)):
        if items_list[j][1] > items_list[i][1]:
            items_list[i], items_list[j] = items_list[j], items_list[i]
print("Sorted by frequency:")
for item, count in items_list:
    print(item, count)

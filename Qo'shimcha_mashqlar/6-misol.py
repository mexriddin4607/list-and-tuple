list_1 = [[1, 2, 4, 5], [44, 65, 43, 11], ["apple", "orange", True, False]]

list_2 = []

for items in list_1:
    list_2.append(items[len(items) - 1])

tuple_1 = tuple(list_2)

print(tuple_1)
list = 21, 33, "mexriddin", True, False, 33.5, 44.6, "apple"


list_1 = []

for element in range(0, 8, 2):
    if element % 2 == 0:
        list_1.append(list[element])

list = tuple(list)
print(list)
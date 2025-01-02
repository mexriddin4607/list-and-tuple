list_1 = [12, [1, 4, 6], 4, 5, 7, [4, 11], 7, 8, 9, 33, ["apple", True], 77]


int_list = []
for i in list_1 :
   if type(i) == int :
      int_list.append(i)

print(int_list)
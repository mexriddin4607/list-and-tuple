list = [10, 'hello', 3.14, 'world', 42, 'python', 99]

kattaharfli_list = []
for i in list:
    if isinstance(i, str):
        kattaharfli_list.append(i.upper())
    else:
        kattaharfli_list.append(i)

print(kattaharfli_list)
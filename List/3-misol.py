#3-4-5 xammasi shu kodda mujassam!

list_1 = [-15, 32, "SALOM", "Dunyo", -9, 17, 4.5, -3, "Python Dasturlash", -25]

list_2 = []
for i in list_1:
    if isinstance(i, int) and i > 0:  #
        list_2.append(i)
    elif isinstance(i, str):  # Stringlarni kichik harfga aylantirildi
        list_2.append(i.lower())

print(list_2)
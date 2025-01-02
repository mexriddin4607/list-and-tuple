qator = "Python and data structures are interesting!"

list_qator = list(qator)

kichik_harflar = []
for i in list_qator :
   if i.islower():
      kichik_harflar.append(i)

print(kichik_harflar)
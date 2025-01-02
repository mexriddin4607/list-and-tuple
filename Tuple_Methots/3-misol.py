#3-4-5 xammasi
raqamlar = (10, 20, 30, 20, 40, 10, 20, 50, 10, 10)

takror_sonlari = {}
for i in raqamlar:
    if i in takror_sonlari:
        takror_sonlari[i] += 1
    else:
        takror_sonlari[i] = 1

eng_kop_takrorlangan = max(takror_sonlari, key=takror_sonlari.get)

print("Eng ko'p takrorlangan element:", eng_kop_takrorlangan)
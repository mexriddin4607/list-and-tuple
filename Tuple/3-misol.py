raqamlar = [(10, 20, 30), (40, 50, 60), (70, 80, 30), (90, 100, 30), (110, 120, 130)]

# Bitta umumiy qiymatni qidirish
birlik_raqam = None
for tuple in raqamlar:
    if birlik_raqam is None:
        birlik_raqam = tuple[2]  # Har bir tuplening uchinchi elementi tekshiriladi
    elif birlik_raqam != tuple[2]:
        birlik_raqam = None
        break

print(birlik_raqam)
a = 10
b = 20
c = 30

if a < b and b < c:
    # a va c ning qiymatlarini almashtirildi
    a, c = c, a

print("a:", a)
print("b:", b)
print("c:", c)
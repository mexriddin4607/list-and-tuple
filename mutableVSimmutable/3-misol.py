my_list = [1, 2, 3, 4, 5]

my_tuple = tuple(my_list)

# Tupleni qayta ro'yxatga aylantirildi
new_list = list(my_tuple)

# Ro'yxatning bir elementini o'zgartiryapmiz yani 2-indexni o'zgartiryapmiz
new_list[2] = 99  

# Natijani chop etildi
print("Yangi ro'yxat:", new_list)
text = "Learning Python is fun!"

words_list = text.split()

words_tuple = tuple(words_list)

last_word_index = words_tuple.index(words_tuple[-1])

print("Oxirgi suz:", words_tuple[-1])
print("Oxirgi suz indeks:", last_word_index)
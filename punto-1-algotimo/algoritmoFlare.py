word = input("Ingrese una palabra: ")
word_filtered = ''.join(character for character in word if not character.isspace() and (not character.isdigit() or int(character) <= 5))
characters_vector = list(word_filtered)
print(characters_vector)


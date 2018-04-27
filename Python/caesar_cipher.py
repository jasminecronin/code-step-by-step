import string 

text = str.upper(input("Your message? "))
shift = int(input("Encoding key? " ))

alphabet = string.ascii_uppercase
shift_alph = alphabet[shift:] + alphabet[:shift]

table = str.maketrans(alphabet, shift_alph)

print(text.translate(table))









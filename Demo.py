number_of_word = 0
number_of_letter = 0
number_of_digits = 0

text = input("Input  a text of number: ")

for x in text:
    x = x.lower()
    if 'a'<= x <='z':
        number_of_letter = number_of_letter + 1
    elif '0' <= x <= '9':
        number_of_digits = number_of_digits + 1
    elif x == ' ':
        number_of_word = number_of_word + 1

print(number_of_word+1)
print(number_of_letter)
print(number_of_digits)



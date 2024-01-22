dict = {}

string = input('Enter a string: ')
for letter in string:
    value = string.count(letter)
    if letter not in dict:
        dict[letter] = value

print(dict)
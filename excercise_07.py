array = []

string = input('Enter a string: ')

for i in range(1):
    array.append([])
    for j in range(0, len(string), 3):
        array[i].append(string[j:j + 3])

print(array)
sum = 0

for num in range(5):
    try:
        value = int(input(f'Enter int #{num + 1}: '))
        sum += value
    except ValueError:
        print('Invalid input. Please enter an int.')
        value = int(input(f'Enter int #{num + 1}: '))
        sum += value

print(sum)
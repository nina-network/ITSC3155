n = int(input('Enter a number: '))
list = []

for i in range(n):
    
    element = int(input(f'Enter number {i+1}: '))
    list.append(element)
print(list)

# figure out how to find median
list.sort()
median = int(n/2)
print(list[median])
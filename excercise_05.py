array = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]

row_1 = int(input('Enter row for coordinate 1: '))
col_1 = int(input('Enter column for coordinate 1: '))
array[row_1 - 1][col_1 - 1] = 1

row_2 = int(input('Enter row for coordinate 2: '))
col_2 = int(input('Enter column for coordinate 2: '))
array[row_2 - 1][col_2 - 1] = 1

row_3 = int(input('Enter row for coordinate 3: '))
col_3 = int(input('Enter column for coordinate 3: '))
array[row_3 - 1][col_3 - 1] = 1

for i in array:
    for j in i:
        print(j, end = ' ')
    print()
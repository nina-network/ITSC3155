list = []
new_list = []

for int in range(10):
    value = input(f'Enter integer {int + 1}: ')
    list.append(value)

for i in range(len(list)):
    if list.count(list[i]) == 2 and list[i] not in new_list:
        new_list.append(list[i])
    
print(list)
print(new_list)
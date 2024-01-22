first_list = []
sec_list = []
for i in range(5):
    first_val = int(input('Enter a number for the first list: '))
    first_list.append(first_val)
for i in range(5):
    sec_val = int(input('Enter a number for the second list: '))
    sec_list.append(sec_val)
print(first_list)
print(sec_list)

third_list =[]
for element in first_list:
    if element in sec_list and element not in third_list:
        third_list.append(element)
print(third_list)
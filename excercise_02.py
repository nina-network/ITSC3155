first_string = str(input('Enter the first string: '))
sec_string = str(input('Enter the second string: '))

if len(first_string) < len(sec_string):
    substring = first_string
    string = sec_string
elif len(sec_string) < len (first_string):
    substring = sec_string
    string = first_string

if string.endswith(substring):
    print(substring)
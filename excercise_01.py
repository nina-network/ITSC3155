score = int(input('Enter a grade from 0 to 100: '))
if score <= 100 and score > 90:
    print('Your grade is A')
elif score < 90 and score > 80:
    print('Your grade is B')
elif score < 80 and score > 70:
    print('Your grade is C')
elif score < 70 and score > 60:
    print('Your grade is D')
elif score < 60:
    print('Your grade is F')
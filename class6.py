x = 50
y = 20
if x == y:
    print('x is greater than y')
else:
    print('y is greater than x')
    
if x == y and x < y:
    print('x is greater than y')
else:
    print('y is greater than x')
    
if x != y or x > y:
    print('x is greater than y')
else:
    print('y is greater than x')
    
if x == y:
    print('x is equal to y')
elif x > y:
    print('x is greater than y')
elif x < y:
    print('x is less than y')
else:
    print('value of x invalid')
    
grade = input('Enter your score: ')
if grade.isnumeric():
    pass
    score = int(grade)
    if score < 0 or score > 100:
        print('invalid score, enter number from 0 - 100.')
    else:
        pass
        if score < 40:
            print('Failed, retry the eaxam')
        elif score >= 40 and score <= 50:
            print('Pass')
        elif score >= 50 and score < 70:
            print('Very good result')
        else:
            print("Excelent score, you're a genius")
else:
    print('Error, enter numbers')


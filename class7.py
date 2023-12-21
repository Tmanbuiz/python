'''
CREATE STATE AND CAPITAL
READ IT
UPDATE/EDITT IT
DELETE IT
'''
state_capital = [
    {'state': 'Abia',
    'capital': 'Umiah'},
    {'state': 'Adamawa',
    'capital': 'Yola'},
    {'state': 'Jigawa',
    'capital': 'Jalingo'}, 
    {'state': 'Lagos',
    'capital': 'Ikeja'}, 
    {'state': 'Ogun',
    'capital': 'Abeokuta'}, 
    {'state': 'Ondo',
    'capital': 'Akure'}, 
    {'state': 'Osun',
    'capital': 'Osogbo'}, 
    {'state': 'Oyo',
    'capital': 'Ibadan'}
]

print('Enter Option A -D')
print('A to view the list of state and capital')
print('B to create a new state and capital')
print('C to edit the list of state and capital')
print('D to delete the list of state and capital')
user_input = str(input('Enter Option: ')).casefold()

if user_input == 'a':
    numbering = 0
    for item in state_capital:
        numbering += 1
        print(f'{numbering}. The state - {item["state"]}. The capital - {item["capital"]}')
elif user_input == 'b':
    state = str(input('Enter the new state: '))
    capital = str(input(f'Enter the capital of {state}: '))
    new_state_capital = {
        'state': state,
        'capital': capital
    }
    
    state_capital.append(new_state_capital)
    numbering = 0
    for item in state_capital:
        numbering += 1
        print(f'{numbering}. The state - {item["state"]}. The capital - {item["capital"]}')
        
if user_input == 'c':
    numbering = 0
    for item in state_capital:
        numbering += 1
        print(f'{numbering}. The state - {item["state"]}. The capital - {item["capital"]}')
    edit_number = input('Enter the number of the state to edit: ')
    target_state_capital = state_capital[int(edit_number) -1]
    print('target_state_capital')
    state = input('Enter the right state to edit: ')
    capital = input('Enter the right capital to edit: ')
    
    if state:
        target_state_capital['state'] = state
    if capital:
        target_state_capital['capital'] = capital
        numbering = 0
    for item in state_capital:
        numbering += 1
        print(f'{numbering}. The state - {item["state"]}. The capital - {item["capital"]}')
    
elif user_input == 'd':
    numbering = 0
    for item in state_capital:
        numbering += 1
        print(f'{numbering}. The state - {item["state"]}. The capital - {item["capital"]}')
    delete_number = (input('Enter the number of the state to delete: '))
    if delete_number.isdigit():
        state_capital.pop(int(delete_number) -1)
        numbering = 0
        for item in state_capital:
            numbering += 1
            print(f'{numbering}. The state - {item["state"]}. The capital - {item["capital"]}')
    else:
        print('The input is not valid')
else:
    print('invalid input')
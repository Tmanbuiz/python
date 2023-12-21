#Loop
fruitlist = ['Banana', 'Apple', 'Mangoes', 'Orange', 'Pawpaw']
for fruits in fruitlist:
    print(fruits.upper())

school = 'PARACH'
for p in school:
    print(p, school.index(p))
    
for x in range(1, 10):
    print(x)
    
student1 = {
    'name' : 'Samuel',
    'Age': 54,
    'Favourite' : 'Programming',
    'Status' : 'Single not searching',
    'Genotype' : 'AA',
    'Location' : 'Benin',
    'Siblings' : ['Joshua', 'Mr Money', 'Mr. Tolu']
}

student2 = {
    'name' : 'Tommy',
    'Age': 65,
    'Favourite' : 'Data Analyst',
    'Status' : 'Single not searching',
    'Genotype' : 'AA',
    'Location' : 'Ibadan',
    'Siblings' : ['Jide', 'Janet', 'Titi'] 
}

student3 = {
    'name' : 'David',
    'Age': 65,
    'Favourite' : 'Programming plus',
    'Status' : 'Married and hooked',
    'Genotype' : 'AA',
    'Location' : 'Togo',
    'Siblings' : ['Gbade', 'Lizy', 'Sade']
}

studentlist = [student1, student2, student3]

for student in studentlist:
    print('Hello', student['name'], 'welcome to', school)
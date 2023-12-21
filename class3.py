# """
# Array
# List []: ordered, mutable
# tuple(): Ordered, Immutable
# set{}: unordered
# Dict {}: ordered, Mutable. keys and value
# """
    
# # List
# student = ["Joshua", "Abeeb", "Mr Money", "DA Tee"]
# print(student[-2][2:])

# #Editing List
# #Replacing elements on the list
# student[-2] = 'Samuel'
# print(student)

# #Deleting an element in a list
# student.pop(-2)
# print(student)
# student.remove("Joshua")
# print(student)

# #Tuple
# fruit = ('Orange', 'Apple', 'Banana')
# print(fruit[0])
# print(fruit[-1])

# #Using Insert to copy fruit into the student list
# student.insert(0, fruit[0])
# print(student)

# # student.insert(3, fruit[-1])
# # print(student)

# #adding new element to the student list
# student.append(fruit[-1])

# print(student)
# student.append('James')
# print(student)
# student.pop(-1)
# print(student)

# #inserting the 2nd tuple element at the middle of student list
# # x = len(student)
# # y = x//2
# student.insert(len(student)//2, fruit[1])
# print(student)

######################################9th of oct 2023###############################################
#Set

'''Methods: .copy(), .clear(), .difference() - diference in variable
'''
setlist1 = {'Banana', 'Apple'}
setlist2 = {'Banana', 'Mango'}
a = setlist1.difference(setlist2)
print(a)

#Dictionary
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

a = student1['name']
b = student1['Status']
print(a)
print(b)

studentlist = [student1, student2, student3]
print(studentlist[1]['name'])
v = studentlist[0]['Siblings'][1][3:]
print(v.upper())

#Looping through the dictionary
for v in studentlist:
    # print(v)
    print(v, '\n\n\r')

for x in studentlist:
    print(x['name'], '\n\r\r')
    
for x in studentlist:
    print(x['Siblings'], '\n\r\r')
# # students = {'name' : 'Jide',
# # 'school' : 'parach',
# # 'dec' : 'Tall and Light in complexion'}
# # # print(f'{name} attends {school}.')
# # # print(f'He is {dec}')
# # # print(students)
# # for student in students:
# #     print(f"{student}: {students[student]}" )
# x = 'Hello'
# # x2 = ['H', 'E', 'L', 'L', 'O']
# # X2= []
# # for word in x:
# #     X2.append(word)
# # print(X2)
# # X2.reverse()
# # x3 = ''.join(X2)
# # print(x3)

# X3 = ''
# for x in X2:
#     X3 += x
# print(X3)

    
# a = 0
# while a <10:
#     print(a)
#     a+=1

# x = 'Hello'
# x2 = ['H', 'E', 'L', 'L', 'O']
# X2= []
# for word in x:
#     X2.append(word)
# X2.append('Joshua')
# X2.append('Samuel')
# X2.append('Parach')
# print(X2)
# x3 = ''.join(X2)
# print(x3)
# Students = []
student1 = {
            'Name' : 'Jide',
            'age' : 40,
            'Gender' : 'Male',
            'PhoneNo' : 9065290965, 
            'DOB' : 12-11-1983 }
student2 = {
            'Name' : 'Jide',
            'age' : 35,
            'Gender' : 'Male',
            'PhoneNo' : 7065478907, 
            'DOB' : 1-11-1988
}
student3 = {
            'Name' : 'Slizy',
            'age' : 23,
            'Gender' : 'Female',
            'PhoneNo' : 7087654653, 
            'DOB' : 24-1-2000
}
student4 = {
            'Name' : 'Bello',
            'age' : 30,
            'Gender' : 'Male',
            'PhoneNo' : 9087654534, 
            'DOB' : 12-11-1993
}
student5 = {
            'Name' : 'Tina',
            'age' : 55,
            'Gender' : 'Female',
            'PhoneNo' : 9087654534, 
            'DOB' : 6-10-1968
}

# create a function that take list of dict items and find the students age mean
def calculate_mean_age(student_list):
    total_age = 0
    num_students = len(student_list)

    for student in student_list:
        total_age += student['age']
    return total_age / num_students

# Example list of students
students = [student1, student2, student3, student4, student5]

# Calculate and print the mean age
mean_age = calculate_mean_age(students)
print("Mean age of students:", mean_age)

# create a function that take list of dict items and find the students mean

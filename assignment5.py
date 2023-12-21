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

def cal_x_age(student_list):
    ages = [student['age'] for student in student_list]
    return sum(ages) / len(ages)


students = [student1, student2, student3, student4, student5]

mean_age = cal_x_age(students)
print(f"Mean age of students: {mean_age}")
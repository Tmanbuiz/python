class Student():
    
    def __init__(self, firstName, lastName, age, PhoneNo, DOB):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.PhoneNo = PhoneNo
        self.DOB = DOB
        
    def returnEmail(self):
        return f'{self.firstName.lower()}.{self.lastName.lower()}@parachdschl.com'
    
    def changeDate(self):
    
        day = self.DOB.split('-')[0]
        mon = self.DOB.split('-')[1]
        year = self.DOB.split('-')[2]

    # Remove 0 on the days
        if day.startswith('0'):
            day = day[1:]

    # Remove 0 on the months
        if mon.startswith('0'):
            mon = mon[1:]

    # Putting position on day
        if day.endswith('11') or day.endswith('12') or day.endswith('13'):
            day += 'th'
        elif day.endswith('1'):
            day += 'st'
        elif day.endswith('2'):
            day += 'nd'
        elif day.endswith('3'):
            day += 'rd'
        else:
            day += 'th'

        mon_short_word = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        mon_Sht = mon_short_word[int(mon)-1]
            
        
        print(f'{day}-{mon_Sht}-{year}')
        return f'{day}-{mon_Sht}-{year}'

    
student1 = Student(
    firstName = 'Slizy',
    lastName = 'Jack',
    age = 23,
    PhoneNo  = '07087654653', 
    DOB = '24-01-2000'
)

student2 = Student(
    firstName = 'Jide',
    lastName= 'Gbade',
    age = 35,
    PhoneNo= '07065478907', 
    DOB= '01-11-1988'
)       

student3 = Student(
    firstName = 'Bello',
    lastName= 'Taiwo',
    age = 30,
    PhoneNo = '09087654534', 
    DOB = '12-11-1993'
    )

print(student1.firstName)
print(student2.changeDate())
print(student1.returnEmail())
'''
CREATE A PRODUCT OBJECTS WITH NAME, DESCRITPION, BRAND, MODEL, PRICE, PRICE, DISCOUNT,
CALCULATE THE TOTALNUMBER OF ALL OBECTSPRICE AFTER REMOVING DISCOUNT
'''
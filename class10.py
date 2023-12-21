def greetings(personName, personAge=89, *arg, **kwargs):
    salutation = f'Hello {personName}'
    age = f'You are {personAge} years of age'
    return salutation +  ' ' + age

def printGreet(functionname):
    print(functionname)

printGreet(greetings('David', 56))

def students(Class, Day, *args):
    list = []
    print('\n\n')
    Classschedule = f'student in {Class} have there lectures on {Day}'
    print(Classschedule)
    for eacharg in args:
        list.append(eacharg)
        print(list, '\n This is a new list')


students('Parach', 'Friday', 'James', 'Tasha')


# '''Create a fibonacci sequence of the value of 200, multiply by the 5th number, and divide by 2'''
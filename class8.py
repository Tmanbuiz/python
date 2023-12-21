# Functions- Block of codes that is reusable and only runs whem invoked
#it can accept data, it return data as output

def greeting():
    print("Hello world")
greeting()



def greetings():
    name = 'Parach'
    print('Hello', name)
greetings()

def greet(person):
    print('Hello', person)
greet('Jide')


name = 'John'  #global variable
def test(person):
    school = 'Univerity of Ibadan'
    print(f'{person}, attended {school}')
    print(f'{name} is a friend to {person}')
    
test("jakes")

def add_nums(num1, num2):
    print(num1 + num2)
add_nums(3, 5)
add_nums(4, 6)
add_nums(7, 8)

def sub_nums(num1, num2):
    print(num1 + num2)
add_nums(3, 5)
add_nums(4, 6)
add_nums(7, 8)

def m_nums(num1, num2):
    print(num1 + num2)
m_nums(3, 5)
m_nums(4, 6)
m_nums(7, 8)

def s_nums(num1, num2):
    print(num1 + num2)
s_nums(9, 5)
s_nums(8, 6)
s_nums(9, 6)

def d_nums(num1, num2):
    print(num1 + num2)
d_nums(25, 5)
d_nums(36, 6)
d_nums(45, 8)

usd_ngn = 1100 #rate for usd to naira 1usd = 1100
def conver_usd_ngn(naira):
    print(usd_ngn * naira)
conver_usd_ngn(3) #converting 3usd to naira
conver_usd_ngn(4)
conver_usd_ngn(7)

ngn = 1/1100 #rate for naira to usd 
def convert_ngn_usd(usd):
    usd_ngn = (ngn * usd)
    usd_ngn_r = round(usd_ngn, 1)
    print(usd_ngn_r)
convert_ngn_usd(3000) #converting #3000 to usd
convert_ngn_usd(46000) #converting #46000 to usd
convert_ngn_usd(7900) #converting #7900 to usd


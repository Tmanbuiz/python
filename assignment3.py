
"""Question 1
Given an integer 'n', perform the following conditional actions

If n is odd, print "Weird' 
If n is even and in the inclusive range of 2 to 5, print 'Not Weird'

If n is even and in the inclusive range of 6 to 20, print "Weird"

If n is even and greater than 28, print 'Not Weird'"""


n = input('Enter A Number: ')
def calculate(num):
    try:
        num = int(num) 
        if num % 2 == 1:
            print("Weird")
        elif num % 2 == 0 and 2 <= num <= 5: # 
            print("Not Weird")
        elif num % 2 == 0 and 6 <= num <= 20:
            print("Weird")
        elif num % 2 == 0 and num > 20:
            print("Not Weird")
    except TypeError:
        print("Value entered is not a number")
    except:
        print('An error occur')
    req = input('Run application again, y for yes any other key for no: ')
    if req.casefold() == 'y':
        calculate(input('enter a number: '))
calculate(n)


# '''
# Question 2

# For this challenge you need to write a program that will display all the numbers between 1 to 100.

# 1 - For each number divisible by 3, the computer should display the word "Fizz". 
# 2- For each number divisible by 5, the computer will display the word "Buzz".

# 3- For each number divisible by both 3 and 5, the computer will display the word "Fizz-Buzz"'''
# numb = input('Enter a number: ')
# def check(n):
#     try:
#         n = int(n)
#         if 1 <= n <= 100:
#             print(n)
#             if n%3 == 0 and n%5 == 0:
#                 print("Fizz-Buzz")
#             elif n%3 == 0:
#                 print("Fizz")
#             elif n%5 == 0:
#                 print("Buzz")
#         else:
#             print('Number must be between 1 and 100')
#     except TypeError:
#         print('Enter number only, nothing else')
#     except:
#         print('Invalid input')
#     again = input('Enter Y to continue or any other key to end: ')
#     if again.upper() == 'Y':
#         print(check(input('Enter Number: ')))
# check(numb)

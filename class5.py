tuple1 = ('Parach', 'Joshua', 42, ['Hello', 'World'])
tuple2 = (1, 2, 3, 4, 5)

# print(tuple1 + tuple2)
str1 = ''
for i in tuple1:
    str1 = str1+ str(i) + ','
a = str1.split(',')
a.pop()
print(a)
# mathResult = int(input('enter student math result: '))
# EnglishResult = int(input('enter English result: '))
# result = mathResult + EnglishResult
# print(result)
x = 5
while x < 10:
    print(x)
    #break
    x += 1
    

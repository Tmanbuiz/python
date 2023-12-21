# import mysql.connector
# database = mysql.connector.connect(host='localhost', user='root', password='shekt080', database='class16_mysql_db')
# action = database.cursor()
# #action.execute("CREATE TABLE products, product_id name VARCHAR(50), description VARCHAR(200), price INT, discount INT, new_price INT")
# action.execute("SHOW TABLES")
# # for table in action:
# #     print(table)

# print('\nTable created')

# create = 'INSERT INTO class16_mysql_db (product_name, description, price, discount, new_price) VALUES(%s, %s, %s, %s, %s)'


age = int(input('Enter your Age: '))
if  0 > age <= 12:
    print('You are child')
elif 13 > age =< 20:
    print('You are a teen')
else:
    print('You are an adult')
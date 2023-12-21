item1 = ['apple', 'orange', 'pine', 'mango', 'banana', 'cherry']
item2 = ['peas', 'beans', 'nut', 'maize', 'peanut', 'wheat']
item3 =[]
def fruit_O(item1, item2):
    if type(item1) != list or type(item2) != list:
        print('The first parameter must be a list')
    else:
        for item in item1:
            # index = item1.index(item)
            if item1.index(item)%2 == 1:
                item3.append(item)
        for items in item2:
            # index = item1.index(item)
            if item2.index(items)%2 == 1:
                item3.append(items)    
        
        return (item3)
    
                
def loopAlist(items): # loop over items in our fruit_O list then overriding the exceptions(errors)
    try:
        for item in items:
            print(item)
    except:
        print('check your input')
        
# fruit_O(item1, item2)
loopAlist(fruit_O(item1, item2))

collect = input('enter a number: ')
try:
    result = int(collect) / 2
    print(result)
except NameError:
    print('wrong number input')
except ValueError:
    print('wrong number input')
except:
    print('wrong input value')
finally:
    print('done')
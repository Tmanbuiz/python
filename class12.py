def recursive_funct(option):
    if option.isalpha():
        print('The recursive function have been called ')
        recursive_funct(input("Enter another command: "))
    else:
        print('The end of the recursive function')
        
def destroyer():
    print('The destructor have been called')
    destroyer()


recursive_funct(input("Enter a command: "))
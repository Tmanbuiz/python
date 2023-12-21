# Temperature converter
#Gradding System


####Start########Temperature converter########################Start####Temperature converter#############
'''Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32.
Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.'''

def temp_f_to_c(cel): #Temperature in degrees Celsius to degrees fahrenheit
    fa = (cel * 9/5 + 32)
    print(f'{fa}°F')
    
temp_f_to_c(5)

def temp_c_to_f(fah): #Temperature conversion from degrees Fahrenheit to degrees Celsius
    cl = (fah - 32) * 5/9
    print(f'{cl}°C')
    
temp_c_to_f(5)



'''The formula used to convert temperature from Celsius to Kelvin is K = C + 273.15
The formula used to convert temperature from Kelvin to Celcius is C = K − 273.15
The formula used to convert temperature from Fahrenheit to Kelvin is, K = (F − 32) × 5 ⁄ 9 + 273.15
The formula used to convert temperature from Kelvin to Fahrenheit is, F = (K – 273.15) × 9 ⁄ 5 + 32'''

def temp_c_to_k(celsius): # convert temperature from celsius to kelvin
    k= (celsius + 273.15)
    print(f'{k}K')
temp_c_to_k(500)

def temp_f_to_k(fahrenheit): # convert temperature from Fahrenheit to kelvin
    f= (fahrenheit - 32) * 5/9 + 273.15
    print(f'{f}K')
temp_f_to_k(500)

def temp_k_to_c(kelvin): # convert temperature from kelvin to degrees celcius
    
    c = kelvin - 273.15
    d = round(c, 1)
    print(f'{d}°C')
temp_k_to_c(30)

def temp_k_to_f(Kelvin): # convert temperature from kelvin to degrees fahrenheit
    f= Kelvin + 273.15
    print(f'{f}°F')
temp_c_to_k(500)


##########End#####Temperature converter######################End######Temperature converter##############







#######Start#######Gradding System#####################Start#######Gradding System################
'''
 A1 Excellent 75% --100%

🕴 B2 Very good 70%---74%

🕴 B3 Good 65%--69%

🕴 C4 Credit 60%--64%

🕴 C5 Credit 55% -- 59%

🕴 C6 Credit 50%--54%

🕴 D7 Pass(still failure) 45%--49%

🕴 E8 Pass(still failure) 40%--45%.

🕴F9 Failure 0%--39%.
'''

def calculate_grade(percentage):
    if 75 <= percentage <= 100:
        return "A1 Excellent"
    elif 70 <= percentage <= 74:
        return "B2 Very good"
    elif 65 <= percentage <= 69:
        return "B3 Good"
    elif 60 <= percentage <= 64:
        return "C4 Credit"
    elif 55 <= percentage <= 59:
        return "C5 Credit"
    elif 50 <= percentage <= 54:
        return "C6 Credit"
    elif 45 <= percentage <= 49:
        return "D7 Pass (still failure)"
    elif 40 <= percentage <= 44:
        return "E8 Pass (still failure)"
    elif 0 <= percentage <= 39:
        return "F9 Failure"
    else:
        return "Invalid input"

# Test the function with specific percentages
percentages = [850, 70, 62, 57, 51, 47, 43, 35]
number = 0
for percentage in percentages:
    number += 1
    result = calculate_grade(percentage)
    print(f"{number}. Grade for {percentage}% is: {result}")
print()
    
percentages = [90, 10, 68, 40, 78, 89, 56, 46, 79, 57]
number = 0
for percentage in percentages:
    number += 1
    result = calculate_grade(percentage)
    print(f"{number}. Grade for {percentage}% is: {result}")
print()
##############Gradding System############################Gradding System################
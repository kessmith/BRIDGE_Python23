# Fahren solution
input_celsius = int(input('Enter your celsius value: '))
input_fahr = int(input('Enter your fahr value: '))

fahrenheit_conv_eq = 1.8 * (input_celsius) + 32
celsius_conv_eq = (5/9) * (input_fahr - 32)

print('Our fahrenheit to celsius value is: ', celsius_conv_eq)
print('Our celsius -->fahrenheit value is: ', fahrenheit_conv_eq)

print("************************************************************************************************************")
"""
The code below is to showcase that you can create identify the type associated with your variable 
"""
x = '123'
print(type(x)) # Prints 'str' as the variable x is a string type
print(type(123)) # Prints 'int' as 123 is an integer value so the type associated would be integer

print("************************************************************************************************************")
"""
Miles Questions
"""
user_destination = input('Where are we going: ')
user_miles_driven = float(input('How many miles does it take to get to where you are going: '))
miles_calc = user_miles_driven/60

print(miles_calc, 'hours to drive')

"""
Pythogarem Theorem using (**) arithmetic operators
"""
a = 3
b = 4
c = (a **2) + (b **2)
print(c)
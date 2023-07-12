# Update your_school statement
your_school = 'University of Connecticut'
print('Current Statement: ' , your_school)
your_school = your_school + ' is the #1 ranked Public University in New England'
print('Updated Statement: ', your_school)

print('*************************************************************************************************************************************')

# Update number statement
x = 5
print('Current Value: ', x)
x = x + 5
print('Updated Value: ', x)

print('*************************************************************************************************************************************')

# Turn num_people into a string and add it to a sentence
num_people = 33
print(num_people)
print('There are ' +  str(num_people) + ' in this class right now')

print('*************************************************************************************************************************************')
###  F -> C converter
# Defning my input variables to be determined by user input
# print('Please input your Fahrenhiet value you would like to convert: ', end='')
# input_celsius = int(input())
# print('Please input your Celsius value you would like to convert: ', end='')
# input_fahren = int(input())

# fahrenheit_conv_eq = 1.8 * (input_celsius) + 32
# celsius_conv_eq = (5/9) * (input_fahren - 32)

# print("Celsius --> Fahrenheit: ", round(fahrenheit_conv_eq, 3)) 
# print("Fahrenheit --> Celsius: ", round(celsius_conv_eq, 3 ))

print('*************************************************************************************************************************************')
# Object Types
x = 'Hello World'
print(x)
print(type(x))
numerical_val = '123'
print(type(numerical_val))
numerical_val = int(numerical_val)
print(type(numerical_val))

print('*************************************************************************************************************************************')
# Floating Point Example
user_destination = input('Where are we going to: ')
user_miles_driven = float(input('How many miles does it take to get to your destination: '))
miles_calc = user_miles_driven/60 # Assumes the speed limit is 60 miles per hour the entire way

print('I would be driving ' + str(user_miles_driven) + ' miles')
print(miles_calc, 'hours to drive')


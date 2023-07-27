'''
Question #1
Take the following output and convert it so it looks like the figure on the below. 
The only expectation with the updated output is that you can only use 1 print() statement so you must use a newline character without to successfully get the correct output
'''
print('Kia Smith is inviting you \nto a video meeting. \n\nJoin meeting: \nhttp://www.zoomskype.us/5592 \n\nPhone:\n1-669-555-2634 (San Jose) \n1-929-555-4000 (New York) \n\nMeeting ID: 5592 \n-------------------------\nReminder: 10 min Before')

'''
Question #2:
Create a python script that calculates the c2 in the Pythagorean theorem to be 100.
• Each value within the theorem needs to be a user input and you must print out the input.
• Must calculate both a2 and b2 and print them out.
'''
print() # Adding this print to make the code much more reable for the user
a = int(input('Enter a value for a: '))
b = int(input('Enter a value for b: '))
c_squared = a**2 + b**2
print('C^2 is: ', c_squared)

'''
Question #3:
Examine the below python script(s) and determine the current error being faced. Once you
have determined the fix the code and run it successfully.
'''
# Script #1 - Updated code
print() # Adding this print to make the code much more reable for the user
a = "36"
b = 48
c = int(a) + b
d = int(a) + b
e = a + str(b)

# Script #2 - Updated code
my_school = "UConn"
my_degree = "Engineering"
my_name = 'Keshawn'
my_program = my_name + my_degree
print('My program is: ', my_program)
my_year = "1"
print('I am attending ' + my_school + ' studying ' + my_degree + ' and I am in my ' + my_year + 'st year')

'''
Question #4:
Create a python script that accepts three parameters. The first input would be an integer.
The second input would be a mathematical function (i.e., +, -, /, *). The last parameter would
also be an integer.
i. Example input:
1st input: 6
2nd input: *
3rd input: 4
Output: 24
'''
print() # Adding this print to make the code much more reable for the user
# Default solution --> Most students should have gotten this
integer_input_one = int(input('Enter your first value: '))
math_function = input('Enter a math symbol to use: ')
integer_input_two = int(input('Enter your second value: '))
print(str(integer_input_one), math_function, str(integer_input_two))

# The more complicated way to complete this would be to do the following:
if math_function == '+':
    solution = integer_input_one + integer_input_two
    print(solution)
elif math_function == '-':
    solution = integer_input_one - integer_input_two
    print(solution)
elif math_function == '/':
    solution = integer_input_one/integer_input_two
    print(solution)
elif math_function == '*':
    solution = integer_input_one * integer_input_two
    print(solution)
else:
    print("The math function inserted does not match anything within our system. Please try again!")

'''
Bonus Question:
Create a function in Python that accepts two parameters. The first should
be the full price of an item as an integer. The second should be the discount percentage as
an integer.
i. Example: The function should return the price of the item after the discount has been
applied. For example, if the price is 100 and the discount is 20, the function should
return 80.
'''
print() # Adding this print to make the code much more reable for the user
full_item_price = int(input('Enter the full item price of your item: '))
discount_percent = int(input('Enter the discount applied to your item: '))

discount_amount = full_item_price * (discount_percent/100)
new_item_price = full_item_price - discount_amount
print('Your new item price is $' + str(new_item_price) + ' post discount')
'''
Question #1:
Create a python program, that calculates my yearly, monthly, and bi-weekly (every 2 weeks per month) incomes based upon the following information:
Hourly Wage = $55 per hour
Hours worked per week = 40 hours
I work a standard 5 days per week.
'''
hourly_wage = 55
hours_worked_per_week = 40

# Option #1
bi_weekly_income_opt1 = hourly_wage * hours_worked_per_week * 2
monthly_income_opt1 = bi_weekly_income_opt1 * 2
yearly_income_opt1 = monthly_income_opt1 * 12

# Option #2:
yearly_income_opt2 = hourly_wage * hours_worked_per_week * 52
monthly_income_opt2 = yearly_income_opt2//12
bi_weekly_income_opt2 = monthly_income_opt2//2

print('Bi-Weekly Income (Option #1): ', bi_weekly_income_opt1) 
print('Monthly Income (Option #1): ', monthly_income_opt1)
print('Yearly Income (Option#1): ', yearly_income_opt1)

print('\nBi-Weekly Income (Option #2): ', bi_weekly_income_opt2) 
print('Monthly Income (Option #2): ', monthly_income_opt2)
print('Yearly Income (Option#2): ', yearly_income_opt2)

'''
Question #2:
Based upon the below code snippets, copy the code and determine the error that is currently being faced. Or determine why the error that is present is currently happening.
'''
# Code Snippet #1 Solution:
print('Current salary is', end=' ') 
print(45000) 
print('Enter new salary:', end=' ') 
new_sal = int(input()) 
print(new_sal)

# Code Snippet #2 Solution:
print('Salary is', end=' ') 
print(20 * 40 * 50) 
print('Enter string: ', end='') 
user_num = str(input()) 
print(user_num)

'''
Question #3:
Create a python program, that generates random numbers for two variables within the
below ranges and then use said values to calculate the c^2 and c value in the Pythagorean
theorem equation.
'''
import random
import math

a = random.randint(3, 7)
print("A's value is: ", a)

b = random.randint(10, 15)
print("B's value is: ", b)

c_squared = a**2 * b**2
print("c^2 is:", c_squared)
c = math.sqrt(c_squared)
print("C's value is: ", c)

'''
Question #4:
Create a python program, that calculates the area of a cylinder based upon the below input values.
'''
r = int(input('Enter radius value: '))
h = int(input('Enter height value: '))
volume = math.pi * (r**2) * h
print('The volume of the cylinder is: ', volume)

'''
Question #5: Bonus Question
Create a python program, that randomly determines my chances of winning a chess match between 0 and 100 and prints the value out
'''
print(f'My chances of winning a chess match is at {random.randint(0, 100)}%')

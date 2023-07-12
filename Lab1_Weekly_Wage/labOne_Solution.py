# If I work 40 hours a week and my hourly wage is $32 an hour. 
# For the entire year (52 weeks) what would be my yearly salary and monthly and bi-weekly income?

hours_work_per_week = 40 # This variable showcases hours worked per week
hourly_wage = 32 # This is my hourly wage
weeks_in_year = 52 # This is the # of weeks in the year

yearly_salary = hours_work_per_week * hourly_wage * weeks_in_year

# Option 1: Monthly Salary
monthly_salary_opt_one = hours_work_per_week * hourly_wage * 4
print('This is your monthly salary (opt#1): ', monthly_salary_opt_one)
# Comma (,) allows for strings and integers to be in the same print statement

# Option 2: Monthly Salary
monthly_salary_opt_two = yearly_salary/12
print(monthly_salary_opt_two, ' is my monthly income')

# Bi-weekly
bi_weekly_pay_cycle = weeks_in_year / 2
print(bi_weekly_pay_cycle)
bi_weekly_pay = hours_work_per_week * hourly_wage * bi_weekly_pay_cycle
print(bi_weekly_pay)
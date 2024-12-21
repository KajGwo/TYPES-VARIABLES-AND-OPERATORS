###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.15 
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'

if is_bonus == True:
    total_salary = (basic_salary + (basic_salary * bonus))
else:
    total_salary = basic_salary

print('Basic salary: ', basic_salary)
print('Bonus included? ', is_bonus)
print('Total salary: ', total_salary)
person1_name = input('Enter first person name: ')
person1_age = int(input('Enter first person age: '))
person2_name = input('Enter second person name: ')
person2_age = int(input('Enter second person age: '))
if person1_age >= 18 and person2_age >= 18:
    print('Both ' + person1_name + ' and ' + person2_name + ' are adults')
else:
    print('one of you is not an adult')

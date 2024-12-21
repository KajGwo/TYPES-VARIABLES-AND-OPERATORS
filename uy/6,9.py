age = float(input('Enter dogs age:'))
if age <= 2:
    age = age * 10.5
else:
    age = (((age - 2) * 4) + 21)
print("your dogs age in human years is ", age)


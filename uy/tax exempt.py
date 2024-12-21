age = int(input('Enter age: '))
if age <= 26:
    no_tax = "true"
else:
    no_tax = "false"
print(f'Exemption from paying taxes: {no_tax}')
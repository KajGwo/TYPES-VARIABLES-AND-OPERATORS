###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter second letter: ')
flc = ord(first)
llc = ord(last)
nol = (llc - flc) - 1
print(f'Between {first} and {last} is {nol} letters')
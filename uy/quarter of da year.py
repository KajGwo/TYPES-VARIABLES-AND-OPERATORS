###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if 12>= month >=10 :
    quarter = 4
elif 9>= month >=7 :
    quarter = 3
elif 6>= month >=4 :
    quarter = 2
elif 3>= month >=1 :
    quarter = 1

print(f'Month {month} is in quarter {quarter}')

# Credit card payment 
#
account_balance = 500
total_payment = float(input('input total due: '))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')
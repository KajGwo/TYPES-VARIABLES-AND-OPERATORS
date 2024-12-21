#
swift = str(input('SWIFT bank code?: '))
print(f'Bank Code: {swift[0:4]} country code: {swift[4:6]} location code: {swift[6:8]} branch code: {swift[8:9]}')

###
# Calculates the sum of even numbers in the range <1,10>
#
sum = 0

for i in range(1,11):
    if not i%2 == 1:
        continue
    sum += 1

print(f'Sum of even numbers in the range <1,10> is {sum}')
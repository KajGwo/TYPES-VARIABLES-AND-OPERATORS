
#BMI CALC

height = input('height in cm: ')
weight = input('weight in kg: ')
height = float(height)
weight = float(weight)
bmi = weight / (height/100)**2
bmi = round(bmi,2)
print('Your BMI is', bmi)
print('Check on the Internet if your BMI is ok!!')

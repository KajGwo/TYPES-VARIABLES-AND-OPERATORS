import math
cm = float(input("how tall r u?: "))
inch = cm * 0.4
feet = inch / 12 
inches = inch % 12 

print(f'I am {cm} cm tall, i.e. {math.floor(feet)} feet and {math.floor(inches)} inches')
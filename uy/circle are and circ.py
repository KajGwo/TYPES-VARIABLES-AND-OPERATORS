
import math###
# Calculation of circle area and circumference 
#

# determine radius and PI values
r = float(input("what is the radius?: "))
# calculate area 
area = (r * r) * math.pi
# calculate circumference 
circ = 2 * math.pi * r
# print results
print("area = ", round(area, 2),"circumfrance =", round(circ, 2))
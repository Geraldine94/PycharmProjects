import math

print ("Please input the radius of the circle")
radio = float(input ("Radio:"))

area = math.pi * radio**2
circumference = 2 * math.pi * radio

print (f"The area is: {area:.2f}")
print (f"The circumference is: {circumference:.2f}")

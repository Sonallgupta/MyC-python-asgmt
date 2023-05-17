#write a Python program which accepts the radius of a circle from the user and computes area.
from math import pi
r = float(input ("Input the radius of the circle : "))
Area = str(pi * r**2);
print ("The area of the circle with radius " + str(r) + " is: " + Area)

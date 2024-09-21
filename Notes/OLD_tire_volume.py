### 
# The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number is the width of the tire in millimeters. The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with a formula, where: v is the volume in liters, π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi), w is the width of the tire in millimeters, a is the aspect ratio of the tire, and d is the diameter of the wheel in inches.
###

import math
print("Tire sizes are always in this format: 205/60R15.  205 = width of the tire (millimeters), 60R is the aspect ratio, and 15 is the diameter (inches) of the wheel.")
w = int(input("Enter the first number - Width of the tire in millimeters: "))
a = int(input("Enter the second number - Aspect ratio, do not include the R "))
d = int(input("Enter the third number - Diameter in inches "))

v = (math.pi * (w ** 2) * a * (w * a + 2540 * d)) / 10000000000

print(f"{v:.2f} liters")

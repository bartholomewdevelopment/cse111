### This program will prompt for three numbers, convert all three numbers into integers, calculate the correct tire volume, print the volume into the terminal with 0, 1 or 2 digits after decimal, import datetime, get current date, print the width, aspect ratio, diameter and volume to volumes.txt file, and showed creativity with the initial statement of what the tire size numbers mean.###
#imports math and datetime libraries
import math
from datetime import datetime

#shows creativity by explaining to the user what the types of numbers mean
print("Tire sizes are always in this format: 205/60R15.  205 = width of the tire (millimeters), 60R is the aspect ratio, and 15 is the diameter (inches) of the wheel.")

#requests the inputs of the numbers from the user
w = int(input("Enter the first number - Width of the tire in millimeters: "))
a = int(input("Enter the second number - Aspect ratio, do not include the 'R': "))
d = int(input("Enter the third number - Diameter in inches: "))

#calculates the volume
v = (math.pi * (w ** 2) * a * (w * a + 2540 * d)) / 10000000000

print(f"{v:.2f} liters")

#pulls current date
current_date_and_time = datetime.now()

#appends the results to the volumes.txt file
with open("volumes.txt", mode="a") as volumes_file:
    volumes_file.write(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}\n")
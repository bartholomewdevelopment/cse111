#Variables
#storage_efficiency
#volume
#surface_area
#radius
#height
#pi


import csv
import math

#constants
pi = math.pi
storage_efficiency = 0
radius = 0
height = 0
can_data = 0

def compute_volume(radius, height):
    #Calculate the cylinder's volume
    return pi * radius**2 * height

def compute_surface_area(radius, height):
    #Calculate the cylinder's surface area
    return 2 * pi * radius * (radius + height)

def main():
    can_data = []
    with open(can_sizes.csv, "r") as file:
        next(file)
        for row in file:
            clean = row.strip()
            data = row.strip().split(',')
            name = data[0]  
            radius = float(data[1])
            height = float(data[2])
            cost = float(data[3])
            can_data.append((name, radius, height, cost))

efficiencies = []
for name, radius, height, cost in can_data:
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    efficiencies.append((name, storage_efficiency, cost))
    print(f'Can: {name}, Volume: {volume:.2f}, Cost: ${cost:.2f}', f'Storage Efficiency: {storage_efficiency:.2f}, Cost: ${cost:.2f}')

main()

def main():
    # Get user input
    starting_odometer = float(input("Enter the starting odometer value (miles): "))
    ending_odometer = float(input("Enter the ending odometer value (miles): "))
    fuel_used = float(input("Enter the amount of fuel used (gallons): "))

    # Calculate fuel efficiency
    mpg = miles_per_gallon(starting_odometer, ending_odometer, fuel_used)
    lp100k = lp100k_from_mpg(mpg)

    # Print results
    print(f"Fuel efficiency: {mpg:.2f} miles per gallon (MPG)")
    print(f"Fuel efficiency: {lp100k:.2f} liters per 100 kilometers (L/100 km)")

def miles_per_gallon(start, end, fuel):
    """Calculate miles per gallon."""
    miles_traveled = end - start
    return miles_traveled / fuel

def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100 kilometers."""
    liters_per_gallon = 3.78541
    kilometers_per_mile = 1.60934
    return (liters_per_gallon / (mpg * kilometers_per_mile)) * 100

# Run the program
if __name__ == "__main__":
    main()

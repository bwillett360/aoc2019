masses = my_string.split("\n")
#masses = ["100756"]
masses = [int(x) for x in masses]
total_fuel_needed = 0

def calc_fuel(mass):
    fuel = int((mass/3)) - 2
    return fuel

for mass in masses:
    done_cal = False
    fuel_needed = calc_fuel(mass)
    while fuel_needed > 0:
        total_fuel_needed += fuel_needed
        fuel_needed = calc_fuel(fuel_needed)

print(total_fuel_needed)

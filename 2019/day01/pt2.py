def calcFuel(module):
    if(module <= 6):
        return 0
    else:
        fuel = int(module / 3) - 2
        fuelForFuel = calcFuel(fuel)
        return fuel + fuelForFuel 

totalFuel = 0
filepath = 'input.txt'
with open(filepath) as fp:
   for count, line in enumerate(fp):
       totalFuel += calcFuel(int(line))

print("fuel total is " + str(totalFuel))
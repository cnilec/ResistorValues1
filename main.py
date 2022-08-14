# This Script asks for bands to be input for a 4 band resistor and provides the Ohm-age with the tolerance

# The Key array defined for lookup - This can be enhanced to be read from disk and put in a param file if needed
lookUpTable = [
               ["RED", 100, 2, "±2%"],
               ["BLUE", 1000000, 6, "±0.25%"],
               ["ORANGE", 1000, 3, "+0%"],
               ["YELLOW", 10000, 4, "+0%"],
               ["VIOLET", 10000000, 7, "±0.1%"],
               ["WHITE", 0, 9, "+0%"],
               ["GREEN", 100000, 5, "±0.5%"],
               ["SILVER", 0.01, 0, "±10%"],
               ["GREY", 0, 8, "±0.05%"],
               ["BLACK", 1, 0, "+0%"],
               ["BROWN", 10, 1, "±1%"],
               ["NONE", 0, 0, "±20%"],
               ["GOLD", 0.1, 0, "±5%"]
               ]
# Initaite Varaibles
FDigit = 0
SDigit = 0
Multiplier = 0
Tolerance = "0"

# Function to validate and return the input color for each Band
# Takes in the value input in first attempt and also takes in the band for the error message
def validateinput(inpvalue, band):
    while inpvalue.upper() not in ["RED", "BLUE", "ORANGE", "YELLOW", "VIOLET", "WHITE", "GREEN", "SILVER", "GREY",
                                   "BLACK", "BROWN",  "NONE", "GOLD"]:
        print("Invalid Color, try again")
        inpvalue = input(band)
    return inpvalue

# Function to lookup the array to get the actual data
# inputs are the value of the band of the color and the subscript defines the data needed in return
def lookup(inpvalue, subscript):
    for x in lookUpTable:
        if x[0] == inpvalue.upper():
            return x[subscript]
    return 0

# Function to calculate the resistance
# it takes the 1st three bands and uses band 1 and band 2 for the value and the 3rd band as the multiploer
def calculateohm(band1, band2, band3):
    return (band1*10+band2)*band3
# the formulae above is band 1 multiplied by 10 and then add the band 2 digit and then use the raw multiplier

#Funtion formats the resistance in text to be printed so that the user knows this KOhm or MOhm etc.
def formatohm(resist):
    if resist >= 1000000:
        ohm = "Mohm"
        resist = resist / 1000000
    elif resist >= 1000:
        ohm = "Kohm"
        resist = resist / 1000
    else:
        ohm = "ohm"

    return str(resist)+" "+ohm


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

# State use cases
    print("For 4 Band resistors - Enter band colors in full in any case")

# First Band Input
    Fst = input("1st Band: ")
    Fst = validateinput(Fst, "1st Band: ")
# Second Band Input
    Snd = input("2nd Band: ")
    Snd = validateinput(Snd, "2nd Band: ")
# Third Band Input
    Trd = input("3rd Band: ")
    Trd = validateinput(Trd, "3rd Band: ")
# 4th Band Input
    Fth = input("4th Band: ")
    Fth = validateinput(Fth, "4th Band: ")

# Get Value of Fist Band which is the fist digit
    FDigit = lookup(Fst, 2)
# Get Value of 2nd Band which is the 2nd Digit
    SDigit = lookup(Snd, 2)
# Get Value of 3rd Band which is the Multiplier
    Multiplier = lookup(Trd, 1)
# Get Value of the 4th Babd whic is the Tolerance
    Tolerance = lookup(Fth, 3)

# Calculate the Resistance in Ohm's
    Resistance = calculateohm(FDigit, SDigit, Multiplier)
# Format the Value in Kilo or Mega Ohms if needed
    FormatResistance = formatohm(Resistance)
# Print the output and you are done
    print("That is", FormatResistance, "with a tolerance of", Tolerance)

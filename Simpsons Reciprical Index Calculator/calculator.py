"""
D = N (N-1)
    --------
    Sum(n(n-1))
Where:
    D = Simpson's Reciprical Index
    N = total number of organisms of all species
    n = number of organisms of a single species
"""

# Calculation Function
def calculateIndex(totalOrganisms, numberSingleSpecies):
    # Top and Bottom values of Equasion
    topValue = float(totalOrganisms * (totalOrganisms-1))
    bottomValue = 0.0

    # Initializes a list that stores the values to sum
    valuesToSum = []

    # Populates values to sum list
    for i in range(len(numberSingleSpecies)):
        temp = numberSingleSpecies[i] * (numberSingleSpecies[i] - 1)
        valuesToSum.append(temp)

    # Sums the list
    for i in range(len(valuesToSum)):
        bottomValue += valuesToSum[i]

    D = float(topValue/bottomValue)
    return D

# Main Function
def main():
    totalOrganisms = 0
    numSpecies = int(input("How many total species were there?\n"))
    speciesValues = []

    for i in range(numSpecies):
        temp = int(input("How many organisms were of species one?\n"))
        speciesValues.append(temp)

    for i in range(len(speciesValues)):
        totalOrganisms += speciesValues[i]

    D = calculateIndex(totalOrganisms, speciesValues)
    print("The total number of organisms is {}".format(totalOrganisms))\

    for i in range(len(speciesValues)):
        print("Number of Species {0}: {1}\n".format(i+1, speciesValues[i]))

    print("The simpsons Reciprical index is {}".format(D))

if __name__ == '__main__':
    decision = input("Do you want to calculate index (y/n)?\n")
    done = False
    while not done:
        if decision == "y" or decision == "Y":
            main()
            decision = input("Do you want to calculate index (y/n)?\n")
        elif decision == "n" or decision == "N":
            done = True
        else:
            print("{} is not an awnser. Please awnser with y or n".format(decision))
            decision = input("Do you want to calculate index (y/n)?\n")

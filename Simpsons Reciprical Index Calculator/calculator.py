import math

"""
D = N (N-1)
    --------
    Sum(n(n-1))

Where:
    D = Simpson's Reciprical Index
    N = total number of organisms of all species
    n = number of organisms of a single species
"""

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

    print(topValue, bottomValue)
    D = float(topValue/bottomValue)
    return D

def main():
    totalOrganisms = float(input('How many total organisms are there?\n'))
    numberSingleSpecies = []

    print("\nPress q to quit\n")
    done = False
    while not done:
        singleSpeciesNumber = input('How many organisms are of one species. (Press q to quit)\n')

        if singleSpeciesNumber == 'q':
            done = True
            break
        elif singleSpeciesNumber != 'q':
            singleSpeciesNumber = int(singleSpeciesNumber)
            numberSingleSpecies.append(singleSpeciesNumber)


    D = calculateIndex(totalOrganisms, numberSingleSpecies)
    print("The simpsons Reciprical index is {}".format(D))

if __name__ == '__main__':
    main()

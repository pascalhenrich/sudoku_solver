import numpy as np

# Sudoku einlesen
def importSudoku():
    input = []
    with open("input.csv") as file:
        for line in file:
            zwischenArray = line.strip().split(",")
            fetigesArray = []
            for i in range(0,9):
                fetigesArray.append(int(zwischenArray[i]))
            input.append(fetigesArray)
    return np.array(input)

# Leere Felder finden
def findEmptyFields(sudo):
    emptyFields = []
    for x in range(0,9):
        for y in range(0,9):
            if sudo[x][y] == 0:
                emptyFields.append((x,y))
    return emptyFields

# Alle Möglichkeiten finden
def getPossibilties(list, sudo):
    dictionary = {}
    for x,y in list:
        noPossibilites = []
        possibilites = []
        # x Achse:
        for i in range(0,9):
            if sudo[x][i]!=0 and sudo[x][i] not in noPossibilites:
                noPossibilites.append(sudo[x][i])
        # y Achse
        for i in range(0,9):
            if sudo[i][y]!=0 and sudo[i][y] not in noPossibilites:
                noPossibilites.append(sudo[i][y])
        # Quadrat
        (qx, qy) = getGrid(x,y)
        for a in range(qx, qx+3):
            for b in range(qy, qy+3):
                if sudo[a][b]!=0 and sudo[a][b] not in noPossibilites:
                    noPossibilites.append(sudo[a][b])
                
        # Update Liste
        for i in range (1,10):
            if i not in noPossibilites:
                possibilites.append(i)
        dictionary.update({(x,y) : possibilites})
    return dictionary

# Hilfsmethode für Quadrat
def getGrid(x,y):
    newX = int(x / 3)
    newY = int(y / 3)
    return (newX*3, newY*3)

# Löst Sudoku
def calculate(sudo):
    empty = findEmptyFields(sudo)
    for (x,y) in empty:
        dictionary = getPossibilties(empty, sudo)
        for element in dictionary[(x,y)]:
            sudo[x][y] = element
            calculate(sudo)
            sudo[x][y] = 0
        return
    print(sudo)

# Main
sudoku = importSudoku()
calculate(sudoku)
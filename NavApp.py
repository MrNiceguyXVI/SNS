#het importeren van libraries
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

#17 x 13// de Kaart die gebruikt word, de nummers
matrix = [
    [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0],
    [0,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0],
    [0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0],
    [0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0]    
]

#veranderd de kaart in een grid
grid = Grid(matrix=matrix)
#print die grid uit
print(grid.grid_str())

#Vraagt de gebruiker om de coordinaten van het start punt in te voeren. en split de resultaten
XStartValue = input("Voer de X en de Y waarde in van het startpunt, gescheden door een spatie: ").split()                #vraagt een input, en splitst die input in 2e, ze worden gesplit op de plek waar een spatie staat

#geeft aan wat de start node is, door de ingevoerede strings naar ints te veranderen
start = grid.node(int(XStartValue[0]),int(XStartValue[1]))

#hetzelde als XStartValue, maar dan voor de eind waarde
XEndValue = input("Voer de x waarde in van het eindpunt, gescheden door een spatie: ").split()

end = grid.node(int(XEndValue[0]),int(XEndValue[1]))

#geeft aan dat de finder niet diagonaal kan bewegen
finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start,end,grid) #activeert het algoritme met de benodigde gegevens: start node, end node, en de Grid

print('Operations: ' + str(runs))                       #print uit door hoeveel iteraties het algoritme is gegaan
print('Path length: ' + str(len(path)) + "\n")          #print uit hoe lang het berekende pad
print(grid.grid_str(path=path, start=start, end=end))   #print de kaart uit, met het start en eind punt, en het pad die het kortste is
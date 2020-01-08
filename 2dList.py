#create 2d list
#create way to have user input start and end 
#find a way to show the indexes of numbers

#17 x 13
X = [
    ["#","#","#","#","#","S"," ","#","#","#","#","#","#","#","#","#","#"],
    ["#"," "," "," ","#"," "," ","#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," ","#"," "," ","#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," ","#"," "," ","#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," ","#"," "," "," "," "," "," "," "," "," "," "," ","#"],
    ["#","#"," ","#","#"," "," ","#","#","#","#","#","#","#","#","#","#"],
    [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
    [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
    ["#","#","#","#","#"," "," ","#","#","#","#","#","#","#"," "," ","#"],
    ["#"," "," "," ","#"," "," ","#"," "," "," "," "," ","#"," "," ","#"],
    ["#"," "," "," ","#"," "," "," "," "," "," "," "," ","#"," "," ","#"],
    ["#"," "," "," "," "," "," ","#"," "," "," "," "," ","#"," "," ","#"],
    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," "," ","#"]    
]

print("0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16\n")
print("\n".join(map('  '.join, X)))          #map functie past de gegeven functie toe op elke iteratie van een list.
                                                #.join veranderd de gegeven list items naar een enkele string, en elk item is gescheiden met het symbool gegeven voor de ., dus " ".join betekent dat elk list item gescheiden word met een 0

startX = input("Voer de X en de Y waarde in van het startpunt, gescheden door een spatie: ").split()                #vraagt een input, en splitst die input in 2e, ze worden gesplit op de plek waar een spatie staat

X[int(startX[1])][int(startX[0])] = "S"                                                                             #veranded het element op de net gegeven coordinaten naar een S, dit staat voor start

eindX = input("Voer de x waarde in van het eindpunt, gescheden door een spatie: ").split()

X[int(eindX[1])][int(eindX[0])] = "E"

print("\n".join(map(' '.join, X)))



#for element in range(8):
    #X[0][element] = "#"
    #X[4][element] = "#"

#for x in range(5):
    #for y in range(7):
        #print() 
        #print(X[x][y]) 
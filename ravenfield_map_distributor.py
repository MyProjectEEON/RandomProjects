import random

plains = ["Nordwind", "Metros","Ampleforth","Jado Industrial (Border Clash)","Costaline","Grove Street"]
forest = ["Grenlau (Wooded Hills)","Rancagua","Coron Industrial (River Delta)","Lastok (Dead City Summer)"]
tundra = ["Cleaver Crest", "Blackwell", "Detsadik", "Nevostok (Dead City Winter)", "Temple", "Ilm (wooded hills snow)"]
ocean = ["Nevent (Island)","Twin Islands","Port Escall (Archipelago)"]
desert = ["A09 Highway","Merian (Canyon)", "Desert Hill","Tavak (Desert Ruins)","Dustbowl","Cenon (Revolt)","Sayom (Lost Village)"]
boss = "Cenon (Revolt)"

biomes = ["plains","forest","tundra","ocean","desert"]
biomeNeighbours = {"plains":["forest","tundra","ocean","desert"],
                   "forest":["plains","tundra"],
                   "tundra":["plains","forest"],
                   "ocean":["plains", "desert"],
                   "desert":["desert"]}

biome = "plains"
conqueredMaps = []
currentMap = ""
nextMap = ""

rush = False

while True:
    if not rush:
        result = input()
    else:
        rush = False
        

    if int(result) >= 2:

        
        if currentMap:
            conqueredMaps.append(currentMap)

            if currentMap == boss:
                print("You Win! #########")
                break

        currentMap = nextMap

        if currentMap != boss:
            nextMap = random.choice(eval(biome))
            while (nextMap in conqueredMaps) or (nextMap == currentMap):
                biome = random.choice(biomeNeighbours[biome])
                nextMap = random.choice(eval(biome))
        else:
            nextMap = "Victory!"
            
        print(currentMap + "  ->  " + nextMap)
        
    elif int(result) <= 1:
        print(currentMap)

        result = input()
        rush = True
        if int(result) <= 1:
            nextMap = currentMap
            
            currentMap = conqueredMaps[-1]
            conqueredMaps.remove(currentMap)



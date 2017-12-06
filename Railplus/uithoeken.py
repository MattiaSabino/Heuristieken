import dictionary

# ZOEKEN NAAR DE UITHOEKEN VAN DE KAART    
uithoeken =[] 
geen_uithoek = 2   

for i in range (b):
    x = stations[i]['Station']
    connecties = len(graph[x])

    if connecties < geen_uithoek:
        uithoeken.append(x)
         


         
         
         
## 
#Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
#Vak: Heuristieken. 
#Case: Rail NL. 
#
#In dit bestand openen we de csv bestanden van stations en verbindingen en laden
#deze in. 
#
##

import csv

def stations(x):

    # Maak een lijst met alle stations, x/y coördinaten en of station kritiek is. 
    stations = []
    with open (x) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations.append(row)
    
    # Return lijst met stations.
    return stations
     
     
def verbindingen(y):

    # Maak een lijst met alle verbindingen en de hoelang deze verbinding duurt.
    verbindingen = []
    with open(y) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            verbindingen.append(row)
    
    # Return een lijst met verbindingen en tijd. 
    return verbindingen


def alle_sporen(stations, verbindingen):

    # Maak een lijst met alle sporen. 
    b = len(stations)
    a = len(verbindingen)
    alle_sporen = []
    
    # Loop door de stations.  
    for i in range (b):  
       
       # Maak een lege lijst met sporen. 
        sporen = [] 
        
        # Loop door de verbindingen.
        for z in range (a):
            
            stat = []
            tijd = []
            
            # Als je de verbinding van een station hebt gevonden voeg deze toe
            # aan lijst met stat. 
            if stations[i]['Station'] == verbindingen[z]['Station1']: 
                stat.append(verbindingen[z]['Station2'])
                
                # Voeg de tijd van de verbinding toe aan tijd.
                tijd.append(verbindingen[z]['Tijd'])
                u = stat, tijd 

                # Voeg de verbinding met station en bijbehorende tijd toe aan 
                # sporen.
                sporen.append(u)
            
            if stations[i]['Station'] == verbindingen[z]['Station2']:
                
                stat.append(verbindingen[z]['Station1'])
                tijd.append(verbindingen[z]['Tijd'])
                u = stat, tijd            
                sporen.append(u)
       
        alle_sporen.append(sporen)
    
    # Return lijst met alle sporen. 
    return alle_sporen
      
      
def graph(stations, alle_sporen):
    
    # Maak lege dict.
    graph = {}
    b = len(stations)
    
    # Vul de dict met stations en alle sporen. 
    for i in range (b):
        y = {}
        x= stations[i]['Station']
        g=alle_sporen[i]
        y = {x:g}
        graph.update(y)
    
    # Return de dict. 
    return graph
    
    
    
def uithoeken(graph, stations):

    # Zoek naar de uithoeken van de kaart.     
    uithoeken =[] 
    
    # Stel uithoek gelijk aan 2.
    geen_uithoek = 2   
    b = len(stations)
    
    # Loop door de stations.
    for i in range (b):
        x = stations[i]['Station']
        connecties = len(graph[x])

        # Als de stations een uithoek is, append aan uithoeken. 
        if connecties < geen_uithoek:
            uithoeken.append(x)
      
    # Return een lijst met uithoeken.     
    return uithoeken
    
    


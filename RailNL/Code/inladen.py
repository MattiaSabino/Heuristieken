import csv

def stations(x):


    # Makes a list with all the stations, x/y cordianates and if it is a critical station.
    stations = []
    with open (x) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations.append(row)

    return stations
           
def verbindingen(y):


    # Makes a list with all the connection and the time.
    verbindingen = []
    with open(y) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            verbindingen.append(row)

    return verbindingen



def alle_sporen(stations, verbindingen):

    b = len(stations)
    a = len(verbindingen)
    alle_sporen = []
    # Prints the station and the connection with the time. 
    for i in range (b):  
       
        sporen = [] 
        for z in range (a):
            
            stat = []
            tijd = []
            
            if stations[i]['Station'] == verbindingen[z]['Station1']:
                
                stat.append(verbindingen[z]['Station2'])
                tijd.append(verbindingen[z]['Tijd'])
                u = stat, tijd            
                sporen.append(u)
              
            if stations[i]['Station'] == verbindingen[z]['Station2']:
                
                stat.append(verbindingen[z]['Station1'])
                tijd.append(verbindingen[z]['Tijd'])
                u = stat, tijd            
                sporen.append(u)
       
        alle_sporen.append(sporen)
        
    return alle_sporen
        
def graph(stations, alle_sporen):
    
    graph = {}
    b = len(stations)
    # Makes the graph
    for i in range (b):
        y = {}
        x= stations[i]['Station']
        g=alle_sporen[i]
        y = {x:g}
        graph.update(y)
    
    return graph
    
    
    
def uithoeken(graph, stations):
    # ZOEKEN NAAR DE UITHOEKEN VAN DE KAART    
    uithoeken =[] 
    geen_uithoek = 2   
    b = len(stations)
    
    for i in range (b):
        x = stations[i]['Station']
        connecties = len(graph[x])

        if connecties < geen_uithoek:
            uithoeken.append(x)
            
    return uithoeken
    
    


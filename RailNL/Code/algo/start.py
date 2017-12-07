from random import randint

def kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations):
    b = len(stations)
    
    # Uithoeken eerst.
    for plek in uithoeken:
        if not plek in trajecten_algemeen:
            z = plek
            trajecten_algemeen.append(z)
            return z

    # Stations die niet zijn aangeraakt komen hierna.
    for i in range (b):
        plek = stations[i]['Station']
        if not plek in trajecten_algemeen:
            z = plek
            trajecten_algemeen.append(z)
            return z

    
    # Niet gereden verbindingen komen als laatst
    for i in range (len(verbindingen)):
        station1 = verbindingen[i]['Station1']
        station2 = verbindingen[i]['Station2']
        verbinding1 = {station1:station2}
        verbinding2 = {station2:station1}
        if not verbinding1 in sporen and not verbinding2 in sporen:
            z = station1
            return z
          
   # Als alles al is geweest
    z = stations[0]['Station']
    return z
    
    
def kies_start2(sporen, verbindingen, uithoeken, trajecten_algemeen, stations):
    
    b = len(stations)
    
    
    for plek in uithoeken:
        if not plek in trajecten_algemeen:
            z = plek
            trajecten_algemeen.append(z)
            return z
            
   # for i in range (b):
     #   plek = stations[i]['Station']
       # if not plek in trajecten_algemeen:
         #   z = plek
           # trajecten_algemeen.append(z)
            #return z

    i = randint(0, len(stations) -1)
    plek = stations[i]['Station']
    z = plek
    if not plek in trajecten_algemeen:
        trajecten_algemeen.append(z)
    return z
    
def kies_start3(sporen, verbindingen, uithoeken, trajecten_algemeen, stations):
        

    i = randint(0, len(stations) -1)
    plek = stations[i]['Station']
    z = plek
    if not plek in trajecten_algemeen:
        trajecten_algemeen.append(z)
    return z
    
    


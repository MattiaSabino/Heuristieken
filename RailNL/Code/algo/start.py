## 
#Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
#Vak: Heuristieken. 
#Case: Rail NL. 
#
#In dit bestand staan de functies van Rail NL. 
#
## 
#Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
#Vak: Heuristieken. 
#Case: Rail NL. 
#
#In dit bestand wordt besloten waar een traject begint.  
#
#
##

from random import randint

# Kies de start, begin altijd bij uithoeken. 
# Begin vervolgens bij station die nog onbereden is. 
# Begin tot slot bij station die nog onbereden sporen heeft.
def kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations):
    b = len(stations)
    
    # Start vanuit de uithoeken. 
    for plek in uithoeken:
    
        # Als uithoek nog niet in trajecten zit, begin in uithoek.
        if not plek in trajecten_algemeen:
            z = plek
            trajecten_algemeen.append(z)
            
            # Return de uithoek, waar wordt begonnen.
            return z

    # Kies hierna stations die niet zijn aangeraakt.
    for i in range (b):
    
        # Als station nog niet in trajecten zit, voeg dit station toe. 
        plek = stations[i]['Station']
        if not plek in trajecten_algemeen:
            z = plek
            trajecten_algemeen.append(z)
            
            # Return station die nog niet aangeraakt is.
            return z

    
    # Kies vervolgens voor station die nog onbereden verbindingen heeft. 
    for i in range (len(verbindingen)):
        station1 = verbindingen[i]['Station1']
        station2 = verbindingen[i]['Station2']
        verbinding1 = {station1:station2}
        verbinding2 = {station2:station1}
        
        # als verbindingen nog niet in sporen zit. 
        if not verbinding1 in sporen and not verbinding2 in sporen:
            z = station1
            
            # Return station met onbereden spoor. 
            return z
          
   # Als alles al is geweest kies willekeurig station. 
    z = stations[0]['Station']
    return z
    
# Pak eerst de uithoeken en dan kies random station.    
def kies_start2(sporen, verbindingen, uithoeken, trajecten_algemeen, stations):
    
    b = len(stations)
    
    # Kies eerst de uithoeken wanneer daar nog niet begonnen is.
    for plek in uithoeken:
        
        # Als uithoek nog niet bereden is. 
        if not plek in trajecten_algemeen:
            z = plek
            trajecten_algemeen.append(z)
            
            # Return station. 
            return z
            
   # for i in range (b):
     #   plek = stations[i]['Station']
       # if not plek in trajecten_algemeen:
         #   z = plek
           # trajecten_algemeen.append(z)
            #return z
    
    # Wanneer op alle uithoeken is begonnen, begin dan random. 
    i = randint(0, len(stations) -1)
    plek = stations[i]['Station']
    z = plek
    
    # Als station nog niet in trajecten zit append deze aan trajecten algemeen.
    if not plek in trajecten_algemeen:
        trajecten_algemeen.append(z)
    return z
  

# Kies hier alle stations waar wordt begonnen random.  
def kies_start3(sporen, verbindingen, uithoeken, trajecten_algemeen, stations):
        
    # Kies random station. 
    i = randint(0, len(stations) -1)
    plek = stations[i]['Station']
    z = plek
    
    # Als station nog niet bereden, voeg toe aan trajecten algemeen.
    if not plek in trajecten_algemeen:
        trajecten_algemeen.append(z)
        
    # Return het station.    
    return z
    
    


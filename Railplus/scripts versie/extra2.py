#TREIN 1
START = start.kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
z = START

thomas = algo1.Trein([START], [START], [z], 0)    

# While loop gaat door tot traject is kleiner of gelijk dan 120.
while (thomas.tijdsduur < MAX):

    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = thomas.opties(sporen, graph, trajecten_algemeen, thomas.eindstation[0])
    #Spoor toevoegen.
    thomas.spoor_toevoegen(sporen, thomas.eindstation[0], beste_optie)
    # Trein verplaatsen naar volgend spoor.
    thomas.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    thomas.actuele_station(beste_optie[0])
    # Tijd updaten.
    thomas.tijd(beste_optie[1])


if thomas.tijdsduur > MAX:
    thomas.verminderen(beste_optie)
    thomas.pop(trajecten_algemeen, sporen)
    lengte = len(thomas.traject) - 1
    thomas.actuele_station(thomas.traject[lengte])
    
    
    
    

    
# TREIN 2
START = start.kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
z = START

bram = algo1.Trein([START], [START], [z],0) 


# While loop gaat door tot traject is kleiner of gelijk dan 120.
while (bram.tijdsduur < MAX):

    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = bram.opties(sporen, graph, trajecten_algemeen, bram.eindstation[0])
    #Spoor toevoegen.
    verbinding = bram.spoor_toevoegen(sporen, bram.eindstation[0], beste_optie)
    # Trein verplaatsen naar volgend spoor.
    bram.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    bram.actuele_station(beste_optie[0])
    # Tijd updaten.
    bram.tijd(beste_optie[1])


if bram.tijdsduur > MAX:
    bram.verminderen(beste_optie)
    bram.pop(trajecten_algemeen, sporen)
    lengte = len(bram.traject) - 1
    bram.actuele_station(bram.traject[lengte])


    
     
#TREIN 3   
START = start.kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
z = START

pau = algo1.Trein([START], [START], [z],0)


while (pau.tijdsduur < MAX):


    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = pau.opties(sporen, graph, trajecten_algemeen, pau.eindstation[0])
    #Spoor toevoegen.
    pau.spoor_toevoegen(sporen, pau.eindstation[0], beste_optie)
    # Trein verplaatsen naar volgend spoor.
    pau.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    pau.actuele_station(beste_optie[0])
    # Tijd updaten.
    pau.tijd(beste_optie[1])


if pau.tijdsduur > MAX:
    
    pau.verminderen(beste_optie)
    pau.pop(trajecten_algemeen, sporen)
    lengte = len(pau.traject) - 1
    pau.actuele_station(pau.traject[lengte])
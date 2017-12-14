## 
#Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
#Vak: Heuristieken. 
#Case: Rail NL. 
#
#In dit bestand staan de functies van Rail NL. 
#
## 

import functies.functies
import algo.start


# Deze functie bepaald het traject. 
def traject_maker(RANGE, MAX, stations, verbindingen, uithoeken, graph, TOTAAL_SPOREN, TOTAAL_STATIONS):

    # Lege lijsten om de gemaakte trajecten in op te slaan. 
    alle_trajecten = []
    trajecten_algemeen =[] 
    sporen = [] 
    alle_tijdsduur = []
    
    
    for i in range (RANGE):

        START = algo.start.kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
        z = START
        
        trein = functies.functies.Trein([START], [START], [z], 0)    

        # While loop gaat door tot traject is kleiner of gelijk dan 120.
        while (trein.tijdsduur < MAX):
        
            if len(sporen) == TOTAAL_SPOREN and len(trajecten_algemeen) == TOTAAL_STATIONS:
                break

            else:
                # Beste optie kiezen aan de hand van de mogelijkheden.
                beste_optie = trein.opties_farest(sporen, graph, trajecten_algemeen, trein.eindstation[0])
                
                #Spoor toevoegen.
                trein.spoor_toevoegen(sporen, trein.eindstation[0], beste_optie)
                
                # Trein verplaatsen naar volgend spoor.
                trein.volgend_spoor(beste_optie[0])
                # Huiding station updaten.
                trein.actuele_station(beste_optie[0])
                # Tijd updaten.
                trein.tijd(beste_optie[1])


        if trein.tijdsduur > MAX:
            trein.verminderen(beste_optie)
            trein.pop(trajecten_algemeen, sporen)
            lengte = len(trein.traject) - 1
            trein.actuele_station(trein.traject[lengte])
        
        
        alle_trajecten.append(trein.traject)
        alle_tijdsduur.append(trein.tijdsduur)

    return alle_tijdsduur, alle_trajecten, sporen, trajecten_algemeen

    
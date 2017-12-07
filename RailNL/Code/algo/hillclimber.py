import algo.start
import functies.functies
import functies.scorefunctie
import functies.minuten


def hillclimber(score1, alle_trajecten1, alle_tijdsduur1, HILL, RANGE, MAX, stations, verbindingen, uithoeken, graph, trajecten_algemeen1, sporen1, TOTAAL_SPOREN, TOTAAL_STATIONS):

    
    for j in range (HILL):
        
        #print("{} out of {}".format(j, HILL))
        
        alle_trajecten = []
        trajecten_algemeen =[] 
        sporen = [] 
        alle_tijdsduur = []
        
        for i in range (RANGE):

            START = algo.start.kies_start2(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
            z = START
            trein = functies.functies.Trein([START], [START], [z], 0)    

            # While loop gaat door tot traject is kleiner of gelijk dan 120.
            while (trein.tijdsduur < MAX):
            
                if len(sporen) == TOTAAL_SPOREN and len(trajecten_algemeen) == TOTAAL_STATIONS:
                    break

                else:

                    # Beste optie kiezen aan de hand van de mogelijkheden.
                    beste_optie = trein.opties(sporen, graph, trajecten_algemeen, trein.eindstation[0])
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
        
        totale_tijdsduur = functies.minuten.minuten(alle_tijdsduur)
        score2 = functies.scorefunctie.score(alle_trajecten, totale_tijdsduur, sporen, TOTAAL_SPOREN)
        
        if len(trajecten_algemeen) == len(stations):
            if score2 > score1:
                score1 = score2
                alle_tijdsduur1 = alle_tijdsduur 
                alle_trajecten1 = alle_trajecten
                trajecten_algemeen1 = trajecten_algemeen
                sporen1 = sporen
            
    return score1, alle_tijdsduur1, alle_trajecten1, sporen1, trajecten_algemeen1
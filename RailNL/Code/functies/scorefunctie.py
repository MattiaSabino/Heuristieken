## 
#Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
#Vak: Heuristieken. 
#Case: Rail NL. 
#
#In dit bestand staat de functie om de score functie mee te berekenen. 
#
#
##

def score(alle_trajecten, totale_tijdsduur, sporen, totaal_sporen):
    
    # Pak allen trajecten.
    s = len(alle_trajecten)
    t = s
    
    # Als de lengte van alle trajecten 1 is, dus trein is nergens heen gegaan. 
    # Tel dit trjaect niet mee. 
    for i in range(s):
        if len(alle_trajecten[i]) == 1:
            t = t-1
    
    # Haal gegevens op van sporen en totale tijdsduur.  
    gebruikte_sporen = len(sporen)
    min = totale_tijdsduur
    
    # Percentage = gebruikte sporen delen door het totaal mogelijke aantal sporen.
    p = gebruikte_sporen / totaal_sporen
    
    # Score functie waarbij p) percentage bereden sporen. t) aantal treinen
    # min) totale tijdsduur. 
    score = p*10000 - (t*20 + min/10000) 
    
    # Return de score. 
    return score
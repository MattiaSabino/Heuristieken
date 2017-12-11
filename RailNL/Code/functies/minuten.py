## 
#Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
#Vak: Heuristieken. 
#Case: Rail NL. 
#
#In dit bestand staat de functie voor het opsommen van aantal minuten. 
#
##

def minuten(alle_tijdsduur):
    
    # Zet totale tijdsduur op 0. 
    totale_tijdsduur = 0
    
    # Tel de tijdsduur van iedere verbinding op bij totale tijdsduur. 
    for i in range(len(alle_tijdsduur)):
        totale_tijdsduur += alle_tijdsduur[i]
    
    # Return de totale tijdsduur. 
    return totale_tijdsduur
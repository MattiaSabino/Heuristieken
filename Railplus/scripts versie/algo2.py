def score(alle_trajecten, totale_tijdsduur, sporen, totaal_sporen):
   

    
    t = len(alle_trajecten)
    
    gebruikte_sporen = len(sporen)
    min = totale_tijdsduur
    p = gebruikte_sporen / totaal_sporen
    
    score = p*10000 - (t*20 + min/10000) 
    
    return score
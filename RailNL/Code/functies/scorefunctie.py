def score(alle_trajecten, totale_tijdsduur, sporen, totaal_sporen):

    s = len(alle_trajecten)
    t = s
    
    for i in range(s):
        if len(alle_trajecten[i]) == 1:
            t = t-1
    
    gebruikte_sporen = len(sporen)
    min = totale_tijdsduur
    p = gebruikte_sporen / totaal_sporen
    
    score = p*10000 - (t*20 + min/10000) 
    
    return score
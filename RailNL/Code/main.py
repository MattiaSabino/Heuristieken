## 
#Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
#Vak: Heuristieken. 
#Case: Rail NL. 
#
#Dit is het main bestand. Run dit bestand door middel van main.py.
#
##

# scorefunctie tot. sporen aanpassen!
import scorefunctie
import trajectmaker
import minuten
import hillclimber
import inladen
import time

# Hou de tijd bij. 
start_time = time.clock()

# Aantal iteraties van de hillclimber.
HILL = 20000

# Zet op maximaal aantal minuten.
MAX = 180

# Zet op maximaal aantal minuten.
RANGE = 8

# Te gebruiken CSV's. 
STATIONS = 'Data/StationsNationaal.csv'
VERBINDINGEN = 'Data/ConnectiesNationaal.csv' 

# Pak de gebruikte lists.
stations = inladen.stations(STATIONS)
TOTAAL_STATIONS = len(stations)

# Laad de verbindingen in. 
verbindingen = inladen.verbindingen(VERBINDINGEN)

# Pak het totaal aantal sporen. 
TOTAAL_SPOREN = len(verbindingen)

# Pak alle sporen. 
alle_sporen = inladen.alle_sporen(stations, verbindingen)

# Laad graph in. 
graph = inladen.graph(stations, alle_sporen)

# Pak alle uithoeken. 
uithoeken = inladen.uithoeken(graph, stations)

# Maak de eerste oplossing en indelen. 
trajecten = trajectmaker.traject_maker(RANGE, MAX, stations, verbindingen, uithoeken, graph, TOTAAL_SPOREN, TOTAAL_STATIONS)
alle_tijdsduur_oud = trajecten[0]
alle_trajecten_oud = trajecten[1]
sporen_oud = trajecten[2]
trajecten_algemeen_oud = trajecten[3]

# Bereken de score.
totale_tijdsduur_oud = minuten.minuten(alle_tijdsduur_oud)
score_oud = scorefunctie.score(alle_trajecten_oud, totale_tijdsduur_oud, sporen_oud, TOTAAL_SPOREN)

# Pas de hillclimber toe.
resultaat = hillclimber.hillclimber(score_oud, alle_trajecten_oud, alle_tijdsduur_oud, HILL, RANGE, MAX, stations, verbindingen, uithoeken, graph, trajecten_algemeen_oud, sporen_oud, TOTAAL_SPOREN, TOTAAL_STATIONS)

# Hill climber returnd 4 gegevens. Deze worden weer opgehaald. 
score = resultaat[0]
alle_tijdsduur = resultaat[1]
alle_trajecten = resultaat[2]
sporen = resultaat[3]
trajecten_algemeen = resultaat[4]
totale_tijdsduur = (minuten.minuten(alle_tijdsduur))


# Deze print statements nog verwijderen. 
print("TRAJECTEN:")
for i in range (len(alle_trajecten)):
    print()
    print("TRAJECT", i)
    print(alle_trajecten[i])
    print(alle_tijdsduur[i])
    
print()
print("SCORE WAS::", score_oud)
print("AANTAL SPOREN WAS::", len(sporen_oud))
print("AANTAL STATIONS WAS::", len(trajecten_algemeen_oud))
print("TOTAAL AANTAL MINUTEN WAS::", totale_tijdsduur_oud)
print()

print()
print("SCORE :::", score)
print("AANTAL SPOREN:: ", len(sporen))
print("AANTAL STATIONS:: ", len(trajecten_algemeen))
print("TOTAAL AANTAL MINUTEN::", totale_tijdsduur)
print()
print(time.clock() - start_time, "seconds")






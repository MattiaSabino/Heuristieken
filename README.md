# Rail NL 

De map heuristieken bevat 3 mappen:
- Psuedocodes: In deze map staan de pseudocodes voor de gebruikte algoritmes.
- RailNL: In deze map staat een nieuwe map met code, verschillende manieren van
het data inladen is hierin te vinden en de resulaten van de algoritmes.
- Visualisaties: In deze map staan de visualisaties van RAIL NL. 

De case Rail NL gaat over het maken van de lijnvoering van intercity treinen in 
Nederland. De case is opgesplitst in twee delen. Allereerst wordt gekeken naar 
de lijnvoering voor Holland, om dit vervolgens uit te breiden naar de lijnvoering 
voor heel Nederland. 
Onder trajecten wordt een route van sporen en stations waarover treinen heen en 
weer rijden, verstaan.

Aantal treinstations in Holland: 22, 
aantal treinstations in Nederland: 61. 

Verder moet er in deze case rekening worden gehouden met 'kritieke stations', 
met bijbehorende 'kritieke sporen'. Wanneer deze stations niet regelmatig worden 
bereden, treden er logistieke problemen op. 

De volgende score functie werd meegegeven bij de case voor de kwaliteit van de 
lijnvoering: 
s = p*10000 - (t*20 + min/100000).
Waarbij:
s = score voor de lijnvoering. 
p = percentage van de bereden kritieke verbindingen. 
t= aantal treinen. 
min = totaal door alle treinen samen gereden minuten in de lijnvoering.

constrains deel 1 - Lijnvoering voor Holland:
1. Tijdsframe van trajecten: maximaal 2 uur. 
2. Alle stations moeten bereden worden binnen de 2 uur. 
3. Maximaal aantal trajecten: 7. 
4. (Alle sporen moeten bereden worden binnen 2 uur met het maximal aantal 
toegestane trajecten).

constrains deel 2 - Lijnvoering voor Nederland:
1. Tijdsframe van trajecten: maximaal 3 uur. 
2. Alle stations moeten bereden worden binnen 3 uur. 
3. Maximaal aantal trajecten: 20. 
4. (Alle sporen moeten bereden worden binnen 3 uur met het maximaal aantal 
toegestane trajecten).

### Voorwaarden

Zorg dat de bijbehorende csv bestanden: ConnectiesHolland.csv, 
StationsHolland.csv voor Holland in dezelfde map staan als het bijbehorende 
python bestand. 
Wanneer wordt gekeken naar heel Nederland moeten de csv bestanden: 
StationsNationaal.csv en ConnextiesNationaal.csv in dezelfde map staan 
als de bijbehorende python bestanden. 

### Installeren

Deze case is gemaakt met behulp van Python 3.6.

#### Runnen:
python main.py

### Probleem type
constrained optimalization problem (COP). Hierbij moet een zo goed mogelijke 
oplossing worden gevonden. 

### Algoritmes

Het eerste algoritme is het Nearest Neighbour algoritme die aan de hand van 
de volgende constrains een lijnvoering maakt:
- Startpunt = uithoeken. 
- Als alle uithoeken geweest zijn: Kies de eerste station die nog niet geweest is
in de lijst. 
- Alle stations geweest? Kies eerste station wiens verbinding nog niet geweest is. 
- Ga dan naar Nearest Neighbour.
- Als station al genomen is: Kies spoor dat nog niet gereden is, meerdere sporen
niet gereden? Kies nearest Neighbour. 
- Alle sporen bereden? Kies nearest Neighbour. 
- Als alleen terug weg mogelijk is? Kies terug weg. (terug weg is laatste keus).
- Traject stopt bij 120 minuten. 
- Als alle sporen & alle stations al zijn geweest: break.
- Pas scorefunctie toe, als het niet nodig was een extra traject te maken, maar
  het wel gebeurd is scorefunctie: trajecten(t) -1.

Het tweede algoritme dat wordt toegepast is een 'hill climber':
Verschil met Nearest Neighbour algoritme is het start punt: 
- Eerst kiest het algoritme de uithoeken. 
- Als alle uithoeken gekozen zijn kies per te maken traject: een random station. 
- Maak traject a.d.h.v. constraints van algoritme 1.
- Pas scorefunctie toe, als het niet nodig was een extra traject te maken, maar
  het wel gebeurd is scorefunctie: trajecten(t) -1.
- Bewaar de betere oplossing.
- Itereer x aantal keer. 


Het derde algoritme dat wordt toegepast is 'simulated annealing'. 



## Auteurs
Paulien Tensen, Matia Caso & Thomas van Dooren. 








# Rail NL 

De case Rail NL gaat over het maken van de lijnvoering van intercity treinen in 
Nederland. De case is opgesplitst in twee delen. Allereerst wordt gekeken naar 
de lijnvoering voor Holland, om dit vervolgens uit te breiden naar de lijnvoering 
voor heel Nederland. 
Onder trajecten wordt een route van sporen en stations waarover treinen heen en 
weer rijden, verstaan.

Aantal treinstations in Holland: 22, 
aantal treinstations in Nederland: 118. 

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

Aangezien 'min' door een heel groot getal gedeeld wordt, is er nauwelijks een 
verandering in de score functie wanneer 'min' veranderd. Vandaar dat we de keuze 
hebben gemaakt 'min' door een kleiner getal te delen, zodat het aantal minuten 
een relevantere rol speelt, in de score functie wanneer 'min' veranderd. Wij 
denken dat dit belangrijk is omdat de trajecttijd ook indiceert of het een goed
traject is of niet. 

Aangepaste score functie: 
s = p*10000 - (t*20 + min/10000)

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

### Toetsingsgrootheid

De toetsingsgrootheid= gemiddelde aantal sporen per station ^(aantal stations), 
in dit geval: 

voor Holland:
2,54 ^ 22 = 806012478.

voor heel Nederland:
2,92 ^ 61 = 1,98 *(10 ^ 28). 

### Probleem type
constrained optimalization problem (COP). Hierbij moet een zo goed mogelijke 
oplossing worden gevonden. 

Aangepaste score functie: s = p*10000 - (t*20 + min/10000).
Orginele score functie: s = p*10000 - (t*20 + min/100000).

#### upperbound: 
Uitkomsten van ons nearest neigbour algoritme:

Holland:
aangepaste score functie:
S-Min = 1 * 10000 - ((6*20) + 672/10000) = 9879,93

orginele score functie:
S-Min = 1 * 10000 - ((6*20) + 672/100000) = 9879,99

Heel Nederland:
aangepaste score functie: 
S-Min = 24/28 * 10000 - ((5*20) + (566/10000) = 8471,37.

orginele score functie:
S-Min = 24/28 * 10000 - ((5*20) + (566/100000) = 8471,42.





#### Lowerbound: Hoogst mogelijke score berekend met de score-functie waarbij 
alle trajecten en stations worden bereden.

Holland: 
381) Aantal minuten samen gereden verbindingen in Holland.
120) Max duur van traject. 
381/120 = 3,175
Theoretische lowerbouwnd) 4 treinen die totaal 381 minuten rijden. 

Aangepaste score functie:
s-Max = 1*10000 -(4*20 + 381/10000) = 9919.9619

Orginele formule: 
s-Max = 1*10000 - (4*20 + (381/100000)) = 9919.99619 


Heel Nederland:
1551) Aantal minuten samen gereden verbindingen in heel Nederland.
180) Max duur van traject.

1551/180 = 8.6.
Theoretische lowerbound) 9 treinen die in totaal 1551 minuten rijden.

Aangepaste formule:
s-Max = 1*10000 - ((9*20) + (1551/10000)) = 9819.8449. 

Orginele formule: 
s-Max = 1*10000 - ((9*20) + (1551/100000)) = 9819.98449.

bron: http://www.thechalkface.net/resources/Travelling_Salesman_England.pdf 

### Algoritmes

In deze case wordt gebruik gemaakt van een ongerichte graaf. Aangezien je heen en weer kunt tussen knopen(stations).
Het tweede algoritme dat wordt toegepast is een 'hill climber'
Het derde algoritme dat wordt toegepast is 'simulated annealing'. 



## Auteurs
Paulien Tensen, Matia Caso & Thomas van Dooren. 








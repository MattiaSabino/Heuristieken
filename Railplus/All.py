
import Nearest_Neighbor



# AUTOMATISEREN: AKA NIET ZELF NAMEN ERIN MOETEN TE DOEN!!::  
# MISSCHIEN OP DEZE MANIER, MAAR BETER KIJKEN NAAR DE LISTS:::::::

trajecten_algemeen =['Amsterdam Centraal']  

START = ['Amsterdam Centraal']       
thomas = Trein(START, START, ['Amsterdam Centraal'], 0)    

#print "TRAJECTEN ALGEMEEN1:: ", trajecten_algemeen 

# While loop gaat door tot traject is kleiner of gelijk dan 120.
while (thomas.tijdsduur < 120):


    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = thomas.opties(thomas.eindstation[0])
    # Trein verplaatsen naar volgend spoor.
    thomas.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    thomas.actuele_station(beste_optie[0])
    # Tijd updaten.
    thomas.tijd(beste_optie[1])

# NIET VERWIJDEREN, BELANGRIJK VOOR ALS DE TRAJECTMAKER GOED WERKT   
#Al is het traject hoger betekent dat er 1 loop te veel gedaan is, dus die moet eraf gehaald worden.

if thomas.tijdsduur > 120:
    thomas.verminderen(beste_optie)
    thomas.pop()
    thomas.pop2()
    lengte = len(thomas.traject) - 1
    thomas.actuele_station(thomas.traject[lengte])
 
# ALGEMENE POP NOG TE DOEN !!!!!! VOOR ALLE TRAJECTEN, ZIE THOMAS _ HAARLEM 
#print "TRAJECTEN ALGEMEEN2:: ", trajecten_algemeen 
 
 

for i in range (b):
    x = stations[i]['Station']
    if not x in trajecten_algemeen:
        START = [x]
        



bram = Trein(START, START, ['Schiphol Airport'],0) 
 
 
 
 
 
# While loop gaat door tot traject is kleiner of gelijk dan 120.
while (bram.tijdsduur < 120):


    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = bram.opties(bram.eindstation[0])
    # Trein verplaatsen naar volgend spoor.
    bram.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    bram.actuele_station(beste_optie[0])
    # Tijd updaten.
    bram.tijd(beste_optie[1])

# NIET VERWIJDEREN, BELANGRIJK VOOR ALS DE TRAJECTMAKER GOED WERKT   
#Al is het traject hoger betekent dat er 1 loop te veel gedaan is, dus die moet eraf gehaald worden.

if bram.tijdsduur > 120:
    bram.verminderen(beste_optie)
    bram.pop()
    bram.pop2()
    lengte = len(bram.traject) - 1
    bram.actuele_station(bram.traject[lengte])  

    
    
   


#print "TRAJECTEN ALGEMEEN voor NU:: ", trajecten_algemeen    

for i in range (b):
    x = stations[i]['Station']
    if not x in trajecten_algemeen:
        START = [x]
        


pau = Trein(START, START, ['Heemstede-Aerdenhout'],0)





while (pau.tijdsduur < 120):

    
    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = pau.opties(pau.eindstation[0])
    # Trein verplaatsen naar volgend spoor.
    
    pau.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    pau.actuele_station(beste_optie[0])
    # Tijd updaten.
    pau.tijd(beste_optie[1])

# NIET VERWIJDEREN, BELANGRIJK VOOR ALS DE TRAJECTMAKER GOED WERKT   
#Al is het traject hoger betekent dat er 1 loop te veel gedaan is, dus die moet eraf gehaald worden.

if pau.tijdsduur > 120:
    pau.verminderen(beste_optie)
    pau.pop()
    pau.pop2()
    lengte = len(pau.traject) - 1
    pau.actuele_station(pau.traject[lengte])   

    
for i in range (b):
    x = stations[i]['Station']
    if not x in trajecten_algemeen:
        START = [x] 
        
        
mat = Trein(START, START, ['Den Helder'],0)





while (mat.tijdsduur < 120):

    
    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = mat.opties(mat.eindstation[0])
    # Trein verplaatsen naar volgend spoor.
    
    mat.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    mat.actuele_station(beste_optie[0])
    # Tijd updaten.
    mat.tijd(beste_optie[1])

# NIET VERWIJDEREN, BELANGRIJK VOOR ALS DE TRAJECTMAKER GOED WERKT   
#Al is het traject hoger betekent dat er 1 loop te veel gedaan is, dus die moet eraf gehaald worden.

if mat.tijdsduur > 120:
    mat.verminderen(beste_optie)
    mat.pop()
    mat.pop2()
    lengte = len(mat.traject) - 1
    mat.actuele_station(mat.traject[lengte])           


for i in range (b):
    x = stations[i]['Station']
    if not x in trajecten_algemeen:
        START = [x] 

        
        
        
        
ben = Trein(START, START, ['Den Helder'],0)

while (ben.tijdsduur < 120):

    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = ben.opties(ben.eindstation[0])
    # Trein verplaatsen naar volgend spoor.
    
    ben.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    ben.actuele_station(beste_optie[0])
    # Tijd updaten.
    ben.tijd(beste_optie[1])

# NIET VERWIJDEREN, BELANGRIJK VOOR ALS DE TRAJECTMAKER GOED WERKT   
#Al is het traject hoger betekent dat er 1 loop te veel gedaan is, dus die moet eraf gehaald worden.

if ben.tijdsduur > 120:
    ben.verminderen(beste_optie)
    ben.pop()
    ben.pop2()
    lengte = len(ben.traject) - 1
    ben.actuele_station(ben.traject[lengte])   

for i in range (b):
    x = stations[i]['Station']
    if not x in trajecten_algemeen:
        START = [x] 


print "TRAJECTEN ALGEMEEN:: ", trajecten_algemeen    
print
print
print
print "TRAJECT THOMAS::", thomas.traject
print
print "TRAJECT BRAM::", bram.traject
print
print "TRAJECT PAU::", pau.traject
print
print "TRAJECT MAT::", mat.traject
print
print "TRAJECT BEN::", ben.traject
    
    

# Class Trein aanmaken.    
class Trein(object):

    def __init__(self, traject, eindstation, beginstation, tijdsduur):
        self.traject= traject
        self.eindstation = eindstation
        self.tijdsduur = tijdsduur
        self.beginstation = beginstation
     
    # Vervang oud station voor huidig station.
    def actuele_station(self,huidig_station):
        self.eindstation = []
        self.eindstation.append(huidig_station)
      
    # Volgend spoor bepalen. 
    def volgend_spoor(self, nieuw_station):
        self.traject.append(nieuw_station)
       
    # Tijd bijhouden.   
    def tijd(self, tijd):
        self.tijdsduur += tijd
    
    # Voeg spoor toe.
    def spoor_toevoegen(self, sporen, huidig_station, beste_optie):
        h = huidig_station
        b = beste_optie[0]
        verbinding1 = {h:b}
        verbinding2 = {b:h}
        
        # Als verbindingen nog niet in sporen zitten, voeg toe aan sporen.
        if not verbinding1 in sporen and not verbinding2 in sporen:
            sporen.append(verbinding1)
        
            
    # Deze functie maakt de beslissing welk spoor er wordt genomen.  
    def opties(self, sporen, graph, trajecten_algemeen, huidig_station):
    
        # Lege lijsten om stations aan toe te voegen. 
        richtingen = graph[huidig_station]
        stations_niet_aangetikt = []
        stations_wel_aangetikt = []
        terugweg = []
        
        for row in richtingen:
            
            # Als de richting nog niet in trajecten zit voeg deze toe aan 
            # stations die nog niet bereden zijn. 
            if row[0][0] not in trajecten_algemeen:
                stations_niet_aangetikt.append(row)
            
            # Als traject niet het begin station is, voeg toe aan terug weg.  
            elif not self.traject == self.beginstation:
                if row[0][0] == self.traject[-2]:
                    terugweg.append(row)
                
                # Anders voeg station toe die al aangetikt is. 
                else:
                    stations_wel_aangetikt.append(row)                                        
            
            # Als traject wel het begin station is, voeg toe aan al bereden 
            # stations.
            else:
                    stations_wel_aangetikt.append(row)
               
        # Als niet bereden stations leeg is. 
        if not stations_niet_aangetikt == []:
            beste_tijd = 1000
            
            # Kies het station met de laagste tijd. 
            for row in stations_niet_aangetikt: 
                if int(row[1][0]) <= beste_tijd:
                    beste_tijd = int(row[1][0])
                    beste_station = row[0][0] 
    
                
            # Voeg best gekozen station toe aan trajecten.     
            trajecten_algemeen.append(beste_station)
            return beste_station, beste_tijd
        
        # Als alle stations zijn bereden. 
        elif not stations_wel_aangetikt == []: 
            
            beste_tijd = 1000
            
            # Manier om sporen te checken. 
            for row in stations_wel_aangetikt:
                
                # Huidig station tegenover optie zetten. 
                h = huidig_station
                b = row[0][0]
                verbinding1 = {h:b}
                verbinding2 = {b:h}

                # Als sporen bij station al zijn bereden.
                if verbinding1 in sporen or verbinding2 in sporen:
                    
                    # Kies spoor met laagste tijd. 
                    if int(row[1][0]) <= beste_tijd:
                        beste_tijd = int(row[1][0])
                        beste_station = row[0][0] 

                # Als spoor nog niet is bereden.         
                else:
                    
                    # Kies beste tijd en station. Return deze.
                    beste_tijd = int(row[1][0])
                    beste_station = row [0][0]
                    return beste_station, beste_tijd
            
            # Return beste station en kortste tijd.
            return beste_station, beste_tijd
            
        # Als terug de enige optie is ga terug.
        else: 
            beste_station = row[0][0]
            beste_tijd =  int(row[1][0])
            return beste_station, beste_tijd
 
    
    # Verwijder laatste verbinding uit lijst trajecten, wanneer tijd is 
    # overschreden.
    def pop(self, trajecten_algemeen, sporen):
      
        a = self.traject[-1]
        b = self.traject[-2]
        laatste_verbinding = {b:a}
        
        # Pop uit trajecten. 
        pop = self.traject.pop() 
        
        # Pop uit trajecten algemeen. 
        pop2 = trajecten_algemeen.pop()
        
        # Als er maar 1 ding in lijst is, kun je niet deze niet verwijderen. 
        if not pop == pop2:
            trajecten_algemeen.append(pop2)
        
        # Verwijder laatste verbinding uit sporen. 
        if laatste_verbinding == sporen[-1]:
            pop3 = sporen.pop()
        
    # Verwijder tijd van laatste verbinding van tijdsduur.     
    def verminderen(self, laatste_verbinding):
        self.tijdsduur -= laatste_verbinding[1] 
        
        
        
        
        
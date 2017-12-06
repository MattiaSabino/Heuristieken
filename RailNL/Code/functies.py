# Trein class aanmaken.    
class Trein(object):

    def __init__(self, traject, eindstation, beginstation, tijdsduur):
        self.traject= traject
        self.eindstation = eindstation
        self.tijdsduur = tijdsduur
        self.beginstation = beginstation
     
    # Vervangt oud station voor huidig station.
    def actuele_station(self,huidig_station):
        self.eindstation = []
        self.eindstation.append(huidig_station)
      
    # Volgend spoor bepalen. 
    def volgend_spoor(self, nieuw_station):
        self.traject.append(nieuw_station)
       
    # Tijd bijhouden.   
    def tijd(self, tijd):
        self.tijdsduur += tijd
    
    def spoor_toevoegen(self, sporen, huidig_station, beste_optie):
        h = huidig_station
        b = beste_optie[0]
        verbinding1 = {h:b}
        verbinding2 = {b:h}
        if not verbinding1 in sporen and not verbinding2 in sporen:
            sporen.append(verbinding1)
        
        

    
        
    # De verbinding met de kortste tijd kiezen.
    # Hier worden alle beslissingen gemaakt kwa welk spoor te nemen
    # Hier moeten dus de restraints aangepast worden!
    def opties(self, sporen, graph, trajecten_algemeen, huidig_station):
    
        richtingen = graph[huidig_station]
        stations_niet_aangetikt = []
        stations_wel_aangetikt = []
        terugweg = []
        
    
        # INDELEN
        for row in richtingen:
            
            #INDELING VAN SPOREN DIE GEREDEN ZIJN MOET NOG GEMAAKT WORDEN
            # MISSCHIEN EEN LIST MET DAARIN DE HUIDIGE SPOOR MET DE UITEINDELIJK 
            # BESTEMMING MAKEN ZODAT WE DAT MAKKELIJK KUNNE CHECKEN
            if row[0][0] not in trajecten_algemeen:
            
             
                stations_niet_aangetikt.append(row)
               
                
                
            elif not self.traject == self.beginstation:
                if row[0][0] == self.traject[-2]:
                    terugweg.append(row)
  
                else:
                    stations_wel_aangetikt.append(row)                                        
                    
            else:
                    stations_wel_aangetikt.append(row)
                    

        #ISGOED!!:: NIET AANGETIKT :: KORSTE VERBINDING
        if not stations_niet_aangetikt == []:
            beste_tijd = 1000
            for row in stations_niet_aangetikt: 
                if int(row[1][0]) <= beste_tijd:
                    beste_tijd = int(row[1][0])
                    beste_station = row[0][0] 
            

           # IDEE OM BIJ TE HOUDEN OF WE ALLE STATIONS HEBBEN GEHAD??
           #if row[0][0] not in self.traject:
                #print row[0][0]
            trajecten_algemeen.append(beste_station)
            return beste_station, beste_tijd

        # ALS ALLE STATIONS ZIJN BEREDEN, KIES NIET DE TERUGWEG.
        # WEL KORTSTE ROUTE VAN DE BEREDEN SPOREN
        
      
        elif not stations_wel_aangetikt == []: 
            
            beste_tijd = 1000
            
            
            for row in stations_wel_aangetikt:
                
                h = huidig_station
                b = row[0][0]
                verbinding1 = {h:b}
                verbinding2 = {b:h}

                

               
                
                if verbinding1 in sporen or verbinding2 in sporen:
                    
                    
                    if int(row[1][0]) <= beste_tijd:
                        beste_tijd = int(row[1][0])
                        beste_station = row[0][0] 
                    
                
                
                
                else:
                    
                    
                    beste_tijd = int(row[1][0])
                    beste_station = row [0][0]
                    return beste_station, beste_tijd
            
            return beste_station, beste_tijd
            
        # ALS TERUG ENIGE OPTIE IS GA TERUG
        else: 
            
            beste_station = row[0][0]
            beste_tijd =  int(row[1][0])
            return beste_station, beste_tijd
 
 
    def pop(self, trajecten_algemeen, sporen):
      
        a = self.traject[-1]
        b = self.traject[-2]
        laatste_verbinding = {b:a}
        
        pop = self.traject.pop() 
        
        pop2 = trajecten_algemeen.pop()
        if not pop == pop2:
            trajecten_algemeen.append(pop2)
      
        if laatste_verbinding == sporen[-1]:
            pop3 = sporen.pop()
        
        
    def verminderen(self, laatste_verbinding):
        self.tijdsduur -= laatste_verbinding[1] 
        
        
        
        
        
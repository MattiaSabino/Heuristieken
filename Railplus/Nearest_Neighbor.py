import dictionary
import uithoeken

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
        

    # De verbinding met de kortste tijd kiezen.
    # Hier worden alle beslissingen gemaakt kwa welk spoor te nemen
    # Hier moeten dus de restraints aangepast worden!
    def opties(self, huidig_station):
       

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
            elif row[0][0] == thomas.traject[-2]:
                terugweg.append(row) 
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
            for row in stations_wel_aangetikt:
                beste_tijd = 1000
                if int(row[1][0]) <= beste_tijd:
                    beste_tijd = int(row[1][0])
                    beste_station = row [0][0]
            return beste_station, beste_tijd
            
        # ALS TERUG ENIGE OPTIE IS GA TERUG
        else: 
            beste_station = row[0][0]
            beste_tijd =  int(row[1][0])
            return beste_station, beste_tijd
 

 
    def pop(self):
        pop = self.traject.pop() 
        
    def pop2(self):
        pop = trajecten_algemeen.pop()
        
    def verminderen(self, laatste_verbinding):
        self.tijdsduur -= laatste_verbinding[1] 
        

        













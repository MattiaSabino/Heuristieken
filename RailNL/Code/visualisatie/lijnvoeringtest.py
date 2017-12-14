
# Course: Huristieken
# Namen: Thomas Van Doren, Mattia Caso, Paulien Tensen. 
# Case: Rail NL
#
# In dit bestand wordt een visualisatie gemaakt van de lijnvoering.
#

import matplotlib.pyplot as plt
import numpy as np
import csv


def visualisatie(x, STATIONS, VERBINDINGEN):
    """"
    Deze functie returned een plotje van de lijnvoering
    m.b.v. matplotlib.
    """
    stations = []
    xcoordinates = []
    ycoordinates = []
    lengte = [] 
    
    # Alle coordinaten van de stations worden ingeladen.
    with open(STATIONS) as f:
        reader = csv.reader(f)
        for row in reader:
            
            stations.append(row[0])
            xcoordinates.append(row[1])
            ycoordinates.append(row[2])
            
    verbinding1 = []
    verbinding2 = []
    somTotaal = 0
    connectiesholland = []

    # 16 kleuren, voor 16 verschillende trajecten.
    colors = ["olive","orange", "green", "blue", "black", "red", "pink","yellow","purple","cyan","brown","magenta","aqua","teal","maroon","fuchsia" ]
    counter = 0

    # Alle verbindingen tussen stations worden ingeladen.
    with open(VERBINDINGEN) as f:
        reader = csv.reader(f)
        
        for row in reader:
            # De eerste row uit reader wordt overgeslagen.
            if counter != 0:
                
                verbinding1.append(row[0])
                verbinding2.append(row[1])
                lengte.append(row[2])

                connectiesholland.append(row)
                
                somTotaal = somTotaal + float(row[2])
            counter +=1
            
    
    # Er wordt een lijnvoering gemaakt van ALLE verbindingen en stations, kleur = grijs.        
    for j in range(0,len(verbinding1)):
            counter1 = stations.index(verbinding1[j])
            verbinding1x = float(xcoordinates[counter1])
            verbinding1y = float(ycoordinates[counter1])
            counter2 = stations.index(verbinding2[j])
            verbinding2x = float(xcoordinates[counter2])
            verbinding2y = float(ycoordinates[counter2])

            plt.plot([verbinding1y,verbinding2y],[verbinding1x,verbinding2x], marker = 'o', color = '0.9')

            # Geen ticks op de y en x as.
            plt.xticks([])
            plt.yticks([])

            # Ga door de lijst met alle trajecten.
            for i in range(0, len(x)):
                
                # Er wordt een lijnvoering gemaakt van de opgegeven trajecten met verschillende kleuren.
                for k in range(0,len(x[i])-1):


                    counterinput1 = stations.index(x[i][k])
                    verbinding1xinput = float(xcoordinates[counterinput1])
                    verbinding1yinput = float(ycoordinates[counterinput1]) 

                    counterinput2 = stations.index(x[i][k+1])
                    verbinding2xinput = float(xcoordinates[counterinput2])
                    verbinding2yinput = float(ycoordinates[counterinput2]) 

                    plt.plot([verbinding1yinput,verbinding2yinput],[verbinding1xinput,verbinding2xinput], marker = 'o', color = colors[i])


    # Weergeef een aantal plaatsnamen om overzicht te krijgen.			
    plt.text(4.5,53, "Den Helder")
    plt.text(3.6,51.3, "Vlissingen")
    plt.text(5.5,51, "Maastricht")
    plt.text(6.7,52, "Enschede")
    plt.text(6.15,53.05, "Groningen")
    plt.text(4.87,51.97, "Utrecht")
    plt.text(5.4,52.57, "Lelystad")
    plt.text(6.23,51.35, "Venlo")
    plt.text(5.29,51.37, "Eindhoven")
    plt.text(4.74,51.53, "Breda")
    plt.text(4.11,52.18, "Den Haag")
    plt.text(6.55,52.47, "Almelo")
    plt.text(6.12, 51.99, "Nijmegen")
    plt.title('Lijnvoering Nederland')
    plt.savefig("test.png")

    plt.show()







    





	
	
	






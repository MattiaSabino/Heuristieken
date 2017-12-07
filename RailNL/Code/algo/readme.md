# Algo

Hierin staan de verschillende algoritmes die gebruikt zijn in Rail NL. 
- Hillclimber: Begint met kies_start2, neemt eerst de uithoeken, dan random.
kies_start 3 wordt gebruikt als experimentatie waarbij elk begin punt random 
wordt gekozen, en geen rekening meer wordt gehouden met uithoeken.
- Start bevat 3 functies: een vaste start (hij pakt eerst de uithoeken, dan 
stations die niet geweest zijn, tot slot stations waarvan de sporen niet bereden
zijn) namen= kies_start, kies_start2, kies_start3.
- Trajectmaker: Maakt een traject aan de hand van kies start.
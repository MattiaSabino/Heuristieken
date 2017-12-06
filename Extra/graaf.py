import csv

alle_sporen = []

# Makes a list with all the stations, x/y cordianates and if it is a critical station.
stations = []
with open ('stations.csv ') as csvfile:
    reader = csv.DictReader(csvfile)
    b = 0
    for row in reader:
        b = b+1
        stations.append(row)
        

# Makes a list with all the connection and the time.
verbindingen = []
with open('verbindingen.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    a = 0
    for row in reader:
        a = a+1
        verbindingen.append(row)


# Prints the station and the connection with the time. 
for i in range (b):  
   
    sporen = [] 
    for z in range (a):
        
        stat = []
        tijd = []
        
        if stations[i]['Station'] == verbindingen[z]['Station1']:
            
            stat.append(verbindingen[z]['Station2'])
            tijd.append(verbindingen[z]['Tijd'])
            u = stat, tijd            
            sporen.append(u)
          
        if stations[i]['Station'] == verbindingen[z]['Station2']:
            
            stat.append(verbindingen[z]['Station1'])
            tijd.append(verbindingen[z]['Tijd'])
            u = stat, tijd            
            sporen.append(u)
   
    alle_sporen.append(sporen)

graph = {}

# Makes the graph
for i in range (b):
    b = {}
    x= stations[i]['Station']
    g=alle_sporen[i]
    b = {x:g}
    graph.update(b)
    




def make_traject(graph, start, MAX =120, count  = None, path = []):
    
    path = path + [start]
    cursor = graph[start]
    
    if not graph.has_key(start):
        return []
    
    best_choice = cursor[0][1]
    best_choice = map(int, best_choice)
    
    integ = 0

    while (''.join(cursor[integ][0])) in path:

       
        integ = integ + 1
        
        if integ == len(cursor):
            
            for row in cursor:
                    
                
                    
                time_row = map(int,row[1])
                
                
                if time_row <= best_choice:        
                    
                    
                    
                    best_choice = time_row
                    best_row = ''.join(row[0])
                    
                    

            best_choice = best_choice[0]  
            
            
            
            count += best_choice
            

            if count > MAX:
                
                count -= best_choice
               
                print path
                print count
                
                return path
                return count
                

            else:
                
                newpath = make_traject(graph, best_row, 120, count, path)
            
        else:
   
            best_choice = cursor[integ][1]
            
            best_choice = map(int, best_choice)

    
    for row in cursor:
        
        if ''.join(row[0]) not in path:
            
            time_row = map(int,row[1])    
            if time_row <= best_choice:        
                
                best_choice = time_row
                best_row = ''.join(row[0])
                
    
    best_choice = best_choice[0]  
    count += best_choice

    
    if count > MAX:
        
        count -= best_choice
        print path
        print count
        
        return path
        return count
    
    else:
        newpath = make_traject(graph, best_row, 120, count, path)
   

make_traject(graph, 'Amsterdam Centraal',count=0)






		
    
    

#!/usr/bin/env python 
import csv 

#Open a CSV FILE
reader = csv.reader(open('SacramentocrimeJanuary2006.csv','rU'))

i=0

#Rutina de chequeo x's
if reader > 1:
    print 
else:
    print  "Algo salio mal al conectar con el archivo"
i = 0;
#Recorrer el archivo csv
for row in reader:
    if i > 0:    
        print  "Beat: "+ row[3] 
        break
    else:
        print row
        i += 1




    #+ "Grid: " + row[4] 
    #print "\n"

#Verificando los nuevos branch 


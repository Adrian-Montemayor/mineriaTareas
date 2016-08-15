#!/usr/bin/env python 
import csv 

#Open a CSV FILE
reader = csv.reader(open('SacramentocrimeJanuary2006.csv','rU'))

#Rutina de chequeo x's
if reader > 1:
    print 
else:
    print  "Algo salio mal al conectar con el archivo"


for index,row in enumerate(reader):

    print  "Beat: "+ row[3] + "Grid: " + row[4] 
    print "\n"

#Verificando los nuevos branch 
import csv
import os
def readFile(fileName):

    try:
        with open(fileName, 'rb') as csvfile:
            try:
				reader=csv.reader(csvfile)
				lista = list(reader)
				#Fecha inicial
				dateFirstRow = lista[0][2]
				#Fecha final
				dateLastRow = lista[len(lista)-1][2]

				#PERIODO (INPUT)
				
				while True:
					try:
						firstDateSelect = str(input("Fecha inicial: "))
						lastDateSelect = str(input("Fecha Final:"))
						firstDateSelect = int(firstDateSelect)
						lastDateSelect = int(lastDateSelect)						
						break		
					except:
						os.system("cls")
						print "Ingrese los anios correctamente (puro numero y dentro del rango).."

				firstDateSelect = str(firstDateSelect)
				lastDateSelect = str(lastDateSelect)
				#Si no se pasa ningun valor
				if firstDateSelect == "" or lastDateSelect == "":
					firstDateSelect = dateFirstRow
					lastDateSelect = dateLastRow

				#Validar que las fecha inicial no sea mayor ala final
				if firstDateSelect > lastDateSelect:
					print "La fecha inicial no puede ser mayor que la final."	
					return

				#RAZA DE LA VICTIMA Y DEL SOSPECHOSO (INPUT) y validación
				os.system("cls")
				while True:
					try:
						victimRace = str(input("Raza de la victica (0, 1, 2, 3, 4, 5, 6):"))
						suspectRace = str(input("Raza del sospechoso (0, 1, 2, 3, 4, 5, 6):"))
						victimRace = int (victimRace)
						suspectRace = int(victimRace)
						break
					except:
						os.system("cls")
						print "ingrese los valores correctamente"
				#Volvemos a parsear para poder comparar la lista
				victimRace = str(victimRace)
				suspectRace = str(suspectRace)

				#GENERO DE LA VICTIMA Y DEL SOSPECHOSO (INPUT)
				while True:
					try:
						victimGenre = str(input("Genero de la victima (0, 1, 2, 3, 5, 6):"))
						suspectGenre= str(input("Genero del sospechoso (0, 1, 2, 3, 5, 6):"))
						victimGenre = int(victimGenre)
						suspectGenre = int(suspectGenre)
						break

					except:
						os.system("cls")
						print "Ingrese los valores correctamente"
				victimGenre = str(victimGenre)
				suspectGenre = str(suspectGenre)
				i=0
				Vhombres=0
				Vmujeres=0
				Shombres=0
				Smujeres=0

				for row in range(0,len(lista)):
					if (lista[row][2] >= firstDateSelect) and (lista[row][2] <= lastDateSelect):
						if (lista[row][4] == victimRace or victimRace == "0") and (lista[row][9] == suspectRace or suspectRace == "0"):
							if (lista[row][6] == victimGenre or victimGenre == "0") and (lista[row][11] == suspectGenre or suspectGenre == "0"):
								i+=1
								if lista[row][6] == str(1):
									Vhombres += 1
								if lista[row][6] == str(2):
									Vmujeres += 1
								if lista[row][11] == str(1):
									Shombres += 1
								if lista[row][11] == str(2):
									Smujeres += 1
								print "Year: " + lista[row][2] + " VRaza: " + lista[row][4] + " SRaza: " + lista[row][9] + " VGenero: " + lista[row][6] + " SGenero: " + lista[row][11] +"\n"
				print "Total: " + str(i)
				porcentaje =  int(Vhombres) *  100  / int(i)
				print "\n#Victimas Hombre: " + str(Vhombres) +"| %" + str(porcentaje)
				porcentaje =  int(Vmujeres) *  100  / int(i)
				print "\n#Victimas Mujer: "  + str(Vmujeres) +"| %" + str(porcentaje)
				restantes =  int(i) - (Vhombres + Vmujeres) 
				restantes =  int(restantes) * 100 / int(i)
				print "No definidos: %" + str(restantes)

				porcentaje =  int(Shombres) *  100  / int(i)
				print "\n#Hombres sospechosos: " + str(Shombres) + "| %" + str(porcentaje)
				porcentaje = int(Smujeres) * 100 / int(i)
 				print "\n#Mujeres sospechosos: " + str(Smujeres) + "| %" + str(porcentaje)
 				restantes =  int(i) - (Shombres + Smujeres) 
				restantes =  int(restantes) * 100 / int(i)
				print "No definidos: %" + str(restantes)

				if  int(i) == 0:
					print "No se encontro ni un dato"

            except Exception as e:
                print e
    except Exception:
        print "No existe el archivo " + fileName + " en el directorio."

readFile('Test.csv')

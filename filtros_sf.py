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
				print "Rango de fechas (" + str(dateFirstRow) +" - "+ str(dateLastRow)+")."
				while True:
					try:
						firstDateSelect = input("Fecha inicial: ")
						lastDateSelect = input("Fecha Final: ")
						#Validar que las fecha inicial no sea mayor ala final
						if firstDateSelect > lastDateSelect:
							os.system("cls")
							print "La fecha inicial no puede ser mayor que la final. Intente nuevamente."	
						else:
							if (firstDateSelect >= int(dateFirstRow)) and (lastDateSelect <= int(dateLastRow)):
								break
							else:
								os.system("cls")
								print "Las fechas estan fuera del rango (" + str(dateFirstRow) +" - "+ str(dateLastRow)+"). Intente nuevamente."
					except Exception as e:
						os.system("cls")
						print "Ingrese los anios correctamente (Ej: 1994)."

				firstDateSelect = str(firstDateSelect)
				lastDateSelect = str(lastDateSelect)
				#RAZA DE LA VICTIMA Y DEL SOSPECHOSO (INPUT) y validacion
				while True:
					try:
						os.system("cls")
						victimRace = input("Raza de la victica (0, 1, 2, 3, 4, 5, 6): ")
						suspectRace = input("Raza del sospechoso (0, 1, 2, 3, 4, 5, 6): ")
						if (victimRace >= 0 and victimRace <= 6) and (suspectRace >= 0 and suspectRace <= 6):
							break
						else:
							os.system("cls")
							print "Eliga una raza dentro del rango."
					except:
						os.system("cls")
						print "Ingrese los valores correctamente."
				#Volvemos a parsear para poder comparar la lista
				victimRace = str(victimRace)
				suspectRace = str(suspectRace)

				#GENERO DE LA VICTIMA Y DEL SOSPECHOSO (INPUT)
				while True:
					try:
						os.system("cls")
						victimGenre = input("Genero de la victima (0, 1, 2, 3, 5, 6): ")
						suspectGenre= input("Genero del sospechoso (0, 1, 2, 3, 5, 6): ")
						if (victimGenre >= 0 and victimGenre <= 6) and (suspectGenre >= 0 and suspectGenre <= 6):
							break
						else:
							os.system("cls")
							print "Eliga un genero dentro del rango."
							
					except:
						os.system("cls")
						print "Ingrese los valores correctamente."
				#Volvemos a parsear para poder comparar la lista
				victimGenre = str(victimGenre)
				suspectGenre = str(suspectGenre)

				i=0
				Vhombres=0
				Vmujeres=0
				Shombres=0
				Smujeres=0

				print "<!===============================================!>"
				print "Anio inicial: " + firstDateSelect
				print "Anio final: "+ lastDateSelect
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
								#print "Year: " + lista[row][2] + " VRaza: " + lista[row][4] + " SRaza: " + lista[row][9] + " VGenero: " + lista[row][6] + " SGenero: " + lista[row][11] +"\n"
								print "[" + lista[row][2] + ", Name: " + lista[row][3] + ", RV: " + lista[row][4] + ", GV: " + lista[row][6] + ", RS: " + lista[row][9] + ", GS: " + lista[row][11] + ", Weapon: " + lista[row][15] +"]"

				print "<!===============================================!>"
				print "Total de registros: " + str(i)
				try:
					porcentaje =  float(Vhombres) *  100  / int(i)
				except:
					porcentaje = 0
				print "\nVictimas Hombre: " + str(Vhombres) +" - Porcentaje: %.2f" %porcentaje +"%"
				try: 
					porcentaje =  float(Vmujeres) *  100  / int(i)
				except: 
					porcentaje = 0
				print "\nVictimas Mujer: "  + str(Vmujeres) +" - Porcentaje: %.2f" %porcentaje +"%"
				try:
					restantes =  int(i) - (Vhombres + Vmujeres) 
					restantes =  float(restantes) * 100 / int(i)
				except:
					restantes = 0
				print "No definidos: %.2f" %restantes+ "%"
				try:
					porcentaje =  float(Shombres) *  100  / int(i)
				except:
					porcentaje = 0
				print "\nHombres sospechosos: " + str(Shombres) + " - Porcentaje: %.2f" %porcentaje +"%"
				try: 
					porcentaje = float(Smujeres) * 100 / int(i)
				except:
					porcentaje = 0
 				print "\nMujeres sospechosos: " + str(Smujeres) + " - Porcentaje: %.2f" %porcentaje +"%"
 				try:
 					restantes =  int(i) - (Shombres + Smujeres) 
					restantes =  float(restantes) * 100 / int(i)
				except:
					restantes = 0
				print "No definidos: %.2f" %restantes+ "%"

				if  int(i) == 0:
					print "No se encontro ni un dato"

            except Exception as e:
                print e
    except Exception:
        print "No existe el archivo " + fileName + " en el directorio."

readFile('Test.csv')

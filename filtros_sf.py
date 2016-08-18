import csv

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
				firstDateSelect = str(input("Anio inicial: "))
				lastDateSelect = str(input("Anio final: "))

				#Si no se pasa ningun valor
				if firstDateSelect == "" or lastDateSelect == "":
					firstDateSelect = dateFirstRow
					lastDateSelect = dateLastRow

				#Validar que las fecha inicial no sea mayor ala final
				if firstDateSelect > lastDateSelect:
					print "La fecha inicial no puede ser mayor que la final."
					return

				#RAZA DE LA VICTIMA Y DEL SOSPECHOSO (INPUT)
				victimRace = str(input("Raza de la victica (0, 1, 2, 3, 4, 5, 6):"))
				suspectRace = str(input("Raza del sospechoso (0, 1, 2, 3, 4, 5, 6):"))

				#si no se ingreso la raza de alguno de los dos.
				#el 0 sirve para seleccionar todas las razas
				if victimRace == "":
					victimRace = "0"

				if suspectRace == "":
					suspectRace = "0"

				#GENERO DE LA VICTIMA Y DEL SOSPECHOSO (INPUT)
				victimGenre = str(input("Genero de la victica (0, 1, 2, 3, 5, 6):"))
				suspectGenre = str(input("Genero del sospechoso (0, 1, 2, 3, 5, 6):"))

				#si no se ingreso el genero de alguno de los dos.
				#el 0 sirve para seleccionar todas los generos
				if victimGenre == "":
					victimGenre == "0"

				if suspectGenre == "":
					suspectGenre = "0" 

				i=0
				for row in range(0,len(lista)):
					if (lista[row][2] >= firstDateSelect) and (lista[row][2] <= lastDateSelect):
						if (lista[row][4] == victimRace or victimRace == "0") and (lista[row][9] == suspectRace or suspectRace == "0"):
							if (lista[row][6] == victimGenre or victimGenre == "0") and (lista[row][11] == suspectGenre or suspectGenre == "0"):
								i+=1
				print "Total: " + str(i)
            except Exception as e:
                print e
    except Exception:
        print "No existe el archivo " + fileName + " en el directorio."

readFile('Test.csv')

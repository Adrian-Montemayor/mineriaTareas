import csv
import os
dateFirstRow = 0
dateLastRow = 0

def readFile(fileName):
	try:
		with open(fileName, 'rb') as csvfile:
			try:
				reader = csv.reader(csvfile)
				lista = list(reader)
				#Fecha inicial
				global dateFirstRow
				dateFirstRow = lista[0][2]
				#Fecha final
				global dateLastRow
				dateLastRow = lista[len(lista)-1][2]
				readYears()
			except Exception as e:
				print e
	except Exception:
		print "No existe el archivo " + fileName + " en el directorio."
	

def readYears():
	#PERIODO (INPUT)
	os.system("cls")
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
	readRace()

def readRace():	
	while True:
		try:
			victimRace = input("Raza de la victima (1, 2, 3, 4, 5, 6): ")
			listVR = []
			if isinstance(victimRace, tuple):
				if len(victimRace) <= 6:
					j=0
					for i in victimRace:
						if isinstance(i, int):
							if (i > 0 and i <= 6):
								listVR.append(i)
								j += 1
								#print i
					if len(listVR) != 0:
						break
				else: 
					print "No puede elegir mas de 6 valores a la vez."
			elif isinstance(victimRace, int):
				if (victimRace > 0 and victimRace <= 6):
					listVR.append(victimRace)
					#print listVR
					break
				else:
					print "Fuera de rango."
			else:
				os.system("cls")
				print "No se puede. Intente nuevamente."
		except:
			print "No se puede. Intente nuevamente."
	######################################################################
	while True:
		try:
			suspectRace = input("Raza del sospechoso (1, 2, 3, 4, 5, 6): ")
			listSR = []
			if isinstance(suspectRace, tuple):
				if len(suspectRace) <= 6:
					j=0
					for i in suspectRace:
						if isinstance(i, int):
							if (i > 0 and i <= 6):
								listSR.append(i)
								j += 1
								#print i
					if len(listSR) != 0:
						break
				else: 
					print "No puede elegir mas de 6 valores a la vez."
			elif isinstance(suspectRace, int):
				if (suspectRace > 0 and suspectRace <= 6):
					listSR.append(suspectRace)
					#print listSR
					break
				else:
					print "Fuera de rango."
			else:
				os.system("cls")
				print "No se puede. Intente nuevamente."
		except:
			print "No se puede. Intente nuevamente."
	print listVR
	print listSR
	readGenre()

def readGenre():	
	while True:
		try:
			victimGenre = input("Genero de la victima (1, 2, 3, 4, 5, 6): ")
			listVG = []
			if isinstance(victimGenre, tuple):
				if len(victimGenre) <= 6:
					j=0
					for i in victimGenre:
						if isinstance(i, int):
							if (i > 0 and i <= 6):
								listVG.append(i)
								j += 1
								#print i
					if len(listVG) != 0:
						break
				else: 
					print "No puede elegir mas de 6 valores a la vez."
			elif isinstance(victimRace, int):
				if (victimRace > 0 and victimRace <= 6):
					listVG.append(victimRace)
					#print listVG
					break
				else:
					print "Fuera de rango."
			else:
				os.system("cls")
				print "No se puede. Intente nuevamente."
		except:
			print "No se puede. Intente nuevamente."
	######################################################################
	while True:
		try:
			suspectGenre = input("Genero del sospechoso (1, 2, 3, 4, 5, 6): ")
			listSG = []
			if isinstance(suspectGenre, tuple):
				if len(suspectGenre) <= 6:
					j=0
					for i in suspectGenre:
						if isinstance(i, int):
							if (i > 0 and i <= 6):
								listSG.append(i)
								j += 1
								#print i
					if len(listSG) != 0:
						break
				else: 
					print "No puede elegir mas de 6 valores a la vez."
			elif isinstance(suspectGenre, int):
				if (suspectGenre > 0 and suspectGenre <= 6):
					listSG.append(suspectGenre)
					#print listSG
					break
				else:
					print "Fuera de rango."
			else:
				os.system("cls")
				print "No se puede. Intente nuevamente."
		except:
			print "No se puede. Intente nuevamente."
	print listVG
	print listSG

readFile('crime_sf.csv')
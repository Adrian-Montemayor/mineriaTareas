import os
os.system("cls")
while True:
	try:
		var = input("Raza de la victima (0, 1, 2, 3, 4, 5, 6): ")
		if isinstance(var, tuple):
			if len(var) <= 6:
				array = [""] * len(var)
				j=0
				for i in var:
					if isinstance(i, int):
						if (i >= 0 and i <= 6):
							array[j] = i
							j += 1
				for x in array:
					print x
				break
		elif isinstance(var, int):
			array = var
			print array
			break
		else:
			os.system("cls")
			print "No se puede. Intente nuevamente."
	except:
		print "No se puede. Intente nuevamente."

#Funciona si se pasa solo un entero
#Funciona si se pasan varios enteros
#Solo acepta 6 numeros seguidos Ej. (1,2,3,4,5,6)
#Solo acepta los numeros dentro del rango 0-6
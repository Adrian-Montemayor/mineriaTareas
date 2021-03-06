import csv, sys

#Lectura de datos del diccionario
datos = {}
def readDictionary(fileName):
    try:
        with open(fileName, 'rb') as csvfile:
            try:
                reader = csv.reader(csvfile)
                for row in reader:
                    datos[row[0]] = row[1]
            except Exception as e:
                print e
    except Exception:
        print "No existe el archivo " + fileName + " en el directorio."
        sys.exit(0)

#Lectura de datos del archivo .csv
lista = []
def readData(fileName):
    try:
        with open(fileName, 'rb') as csvfile:
            try:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row[0]) < 16:
                        str1 = row[0][:5]
                        str2 = row[0][8:len(row[0])]
                        if len(str2) < 5:
                            str2 = "0" + row[0][8:len(row[0])]
                        row[0] = "0" + str1 + "2006 " + str2
                    lista.append(row)
            except Exception as e:
                print e
    except Exception:
        print "No existe el archivo " + fileName + " en el directorio."
        sys.exit(0)

#Toma de una lista y te regresa la cantidad de crimenes de la siguientes gravedad para la transicion
def getNextSeverity(row, nextSev):
    numberCrimes = 0
    while row[3] < nextSev - 1:
        row[1] += 1
        row[2] += nextSev
        row[3] = float(row[2]) / float(row[1])
        numberCrimes += 1
        #print row #visualizar transicion
    return numberCrimes

#Toma de una lista y te regresa la cantidad de crimenes de la previa gravedad para la transicion
def getPreviousSeverity(row, prevSev):
    numberCrimes = 0
    while row[3] >= prevSev + 2:
        row[1] += 1
        row[2] += prevSev
        row[3] = float(row[2]) / float(row[1])
        numberCrimes += 1
        #print row #visualizar transicion
    return numberCrimes

readDictionary('words.csv')
readData('crimes.csv')

distritos = [['1', 0, 0, 0], ['2', 0, 0, 0], ['3', 0, 0, 0], ['4', 0, 0, 0], ['5', 0, 0, 0], ['6', 0, 0, 0]]

dateStart = lista[0][0]
dateEnd = lista[len(lista) - 1][0]

#Validar si desea realizar busqueda en base a fechas
dateNeed = ""
while "S" not in dateNeed and "N" not in dateNeed:
    try:
        dateNeed = raw_input("Desea hacer una busqueda en base a fechas? (S/N): ").upper()
        if "S" not in dateNeed and "N" not in dateNeed:
            print "\nDato no aceptable. Intentelo de nuevo."
    except Exception as e:
        print e

if dateNeed == "S":
    dateStartDay, dateStartHour, dateStartMinute = None, None, None
    dateEndDay, dateEndHour, dateEndMinute = None, None, None

    while dateStartDay < 1 or dateStartDay > 31:
        try:
            dateStartDay = int(input("Dia inicial (1 - 31): "))
            if dateStartDay < 1 or dateStartDay > 31:
                print "\nDato no aceptable. Intentelo de nuevo."
        except Exception:
            print "\nDato no aceptable. Intentelo de nuevo."

    while dateStartHour < 0 or dateStartHour > 23:
        try:
            dateStartHour = int(input("Hora inicial (00 - 23): "))
            if dateStartHour < 0 or dateStartHour > 23:
                print "\nDato no aceptable. Intentelo de nuevo."
        except Exception:
            print "\nDato no aceptable. Intentelo de nuevo."

    while dateStartMinute < 0 or dateStartMinute > 59:
        try:
            dateStartMinute = int(input("Minuto inicial (00 - 59): "))
            if dateStartMinute < 0 or dateStartMinute > 59:
                print "\nDato no aceptable. Intentelo de nuevo."
        except Exception:
            print "\nDato no aceptable. Intentelo de nuevo."

    while dateEndDay < dateStartDay or dateEndDay > 31:
        try:
            dateEndDay = int(input("Dia Final (" + str(dateStartDay) + " - 31): "))
            if dateEndDay < dateStartDay or dateEndDay > 31:
                print "\nDato no aceptable. Intentelo de nuevo."
        except Exception:
            print "\nDato no aceptable. Intentelo de nuevo."

    if dateStartDay == dateEndDay:
        dateHour = dateStartHour
    else:
        dateHour = 0

    while dateEndHour < dateHour or dateEndHour > 23:
        try:
            dateEndHour = int(input("Hora Final ("+ str(dateHour) + " - 23): "))
            if dateEndHour < dateHour or dateEndHour > 23:
                print "\nDato no aceptable. Intentelo de nuevo."
        except Exception:
            print "\nDato no aceptable. Intentelo de nuevo."

    if dateStartHour == dateEndHour:
        dateMinute = dateStartMinute
    else:
        dateMinute = 0

    while dateEndMinute < dateMinute or dateEndMinute > 59:
        try:
            dateEndMinute = int(input("Minuto final (" + str(dateMinute) + " - 59): "))
            if dateEndMinute < dateMinute or dateEndMinute > 59:
                print "\nDato no aceptable. Intentelo de nuevo."
        except Exception:
            print "\nDato no aceptable. Intentelo de nuevo."

    dateStart = "01/" + str(dateStartDay).zfill(2) + "/2006 " + str(dateStartHour).zfill(2) + ":" + str(dateStartMinute).zfill(2)
    dateEnd = "01/" + str(dateEndDay).zfill(2) + "/2006 " + str(dateEndHour).zfill(2) + ":" + str(dateEndMinute).zfill(2)

#Validar si desea realizar una busqueda en base a algun distrito, sino districtNumber = 0
districtNeed = ""
while "S" not in districtNeed and "N" not in districtNeed:
    try:
        districtNeed = raw_input("Desea hacer una busqueda en base a algun distrito? (S/N): ").upper()
        if "S" not in districtNeed and "N" not in districtNeed:
            print "\nDato no aceptable. Intentelo de nuevo."
    except Exception:
        print "\nDato no aceptable. Intentelo de nuevo."

#Pide los datos para la busqueda entre un rango de fechas
districtNumber = 0
if districtNeed == "S":
    districtNumber = None
    while districtNumber < 0 or districtNumber > 6:
        try:
            districtNumber = int(input("Que distrito desea visualizar (1 - 6; 0 para todos): "))
            if districtNumber < 0 or districtNumber > 6:
                print "\nDato no aceptable. Intentelo de nuevo."
        except Exception:
            print "\nDato no aceptable. Intentelo de nuevo."

numeroRegistros = 0
for row in lista:
    if (int(row[1]) == districtNumber or districtNumber == 0) and \
    (row[0] >= dateStart and row[0] <= dateEnd):
        numeroRegistros += 1

numberRows = 0
if numeroRegistros == 0:
    print "\nNo existen registros en base a la seleccion actual."
    sys.exit(0)
else:
    while numberRows < 1 or numberRows > numeroRegistros:
        try:
            numberRows = int(input("Cuantos datos desea visualizar (" + str(numeroRegistros) + " registros en total): "))
            if numberRows < 1 or numberRows > numeroRegistros:
                print "\nDato no aceptable. Intentelo de nuevo."
        except Exception:
            print "\nDato no aceptable. Intentelo de nuevo."

print "\n"

print "[Fecha, Distrito, Crimen, Gravedad]"

i = 0
for row in lista:
    if i < numberRows and (int(row[1]) == districtNumber or districtNumber == 0) and \
    (row[0] >= dateStart and row[0] <= dateEnd):
        sumatoria = 0
        for key, value in datos.items():
            if key in row[2]:
                sumatoria += int(value)
        if sumatoria < 1:
            sumatoria = 1
        if sumatoria > 8:
            sumatoria = 8
        distritos[int(row[1]) - 1][1] += 1
        distritos[int(row[1]) - 1][2] += sumatoria
        row.append(sumatoria)
        i += 1
        print row

print "\n"

for row in distritos:
    if int(row[0]) == districtNumber or districtNumber == 0:
        try:
            row[3] = float(row[2]) / float(row[1])
            print "El distrito " + row[0] + " tiene un promedio de gravedad %0.4f" % row[3]
        except Exception:
            print "El distrito " + row[0] + " no presenta registros en la seleccion actual"

print "\n---TRANSICIONES---\n"

#Calcular transicion proxima gravedad
for row in distritos:
    if (int(row[0]) == districtNumber or districtNumber == 0) and row[3] != 0:
        if row[3] <= 7:
            org1, org2, org3 = row[1], row[2], row[3]
            nextSeveri = int(row[3] % 2) + int(row[3]) + 2
            nCrimes = getNextSeverity(row, nextSeveri)
            print "Distrito " + row[0] + " a gravedad " + \
            str(nextSeveri - 1) + ": " + str(nCrimes) + " crimenes de gravedad " + str(nextSeveri)
            row[1], row[2], row[3] = org1, org2, org3
        else:
            print "Distrito " + row[0] + " esta en la gravedad mas alta."
print "\n"

#Calcular transicion gravedad previa
for row in distritos:
    if (int(row[0]) == districtNumber or districtNumber == 0) and row[3] != 0:
        if row[3] >= 3:
            prevSeveri = int(row[3] % 2) + int(row[3]) - 3
            nCrimes = getPreviousSeverity(row, prevSeveri)
            print "Distrito " + row[0] + " a gravedad " + \
            str(prevSeveri + 1) + ": " + str(nCrimes) + " crimenes de gravedad " + str(prevSeveri)
        else:
            print "Distrito " + row[0] + " esta en la gravedad mas baja."

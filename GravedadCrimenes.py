import csv, sys

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

lista = []
def readData(fileName):
    try:
        with open(fileName, 'rb') as csvfile:
            try:
                reader = csv.reader(csvfile)
                for row in reader:
                    lista.append(row)
            except Exception as e:
                print e
    except Exception:
        print "No existe el archivo " + fileName + " en el directorio."
        sys.exit(0)

readDictionary('words.csv')
readData('crimes.csv')

distritos = [['1', 0, 0], ['2', 0, 0], ['3', 0, 0], ['4', 0, 0], ['5', 0, 0], ['6', 0, 0]]
for row in lista:
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

for row in distritos:
    print row

import csv

def readFile(fileName):
    try:
        with open(fileName, 'rb') as csvfile:
            try:
                reader = csv.reader(csvfile)
                for row in reader:
                    print row
            except Exception as e:
                print e
    except Exception:
        print "No existe el archivo " + fileName + " en el directorio."

readFile('Test.csv')

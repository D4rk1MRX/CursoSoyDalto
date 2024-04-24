import csv
with open("archivos\\archivocsv.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
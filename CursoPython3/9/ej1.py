import csv
fichero = open("ejemplo2.csv")  # ejemplo1.csv , ejemplo3.csv
contenido = csv.reader(fichero)
print(list(contenido))
list(contenido)
fichero.close()
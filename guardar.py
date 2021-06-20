"""Guarda datos posprocesados en formato csv."""

import numpy as np
import csv

nombres = ["fila 1", "fila 2"]
datos = np.zeros([5, 2])

print(nombres)
print(datos)

archivo = open("archivo.csv", newline="")
csvwriter = csv.writer(archivo, dialect="excel")
# csvwriter.write(nombres)
"""
for row in datos:
    csvwriter.writerow(row)
"""
archivo.close()

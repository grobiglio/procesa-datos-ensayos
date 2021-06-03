# -*- coding: utf-8 -*-
"""Módulo principal."""

import os
import matplotlib.pyplot as plt
import leer
import posprocesar

os.system('cls')

# nombre_archivo = input("Ingresar nombre de archivo: ")
nombre_archivo = "datos_en_bruto"
# Lectura del archivo .mat y extracción de información del archivo
mat = leer.leer_archivo(nombre_archivo)
key_valor_parametros = mat["__globals__"][0]
key_info_parametros = mat["__globals__"][1]
info_parametros = str(mat[key_info_parametros][0])
frec_muestreo = leer.devolver_frecuencia_de_muestreo(info_parametros)
nombre_parametros = leer.devolver_nombre_parametros(info_parametros)
valor_parametros = mat[key_valor_parametros]
print(f"Se ha leído la información del archivo {nombre_archivo}.mat.")
cant_parametros = len(nombre_parametros)
print(f"El archivo tiene información de {cant_parametros} parámetros.")
print(f"La frecuencia de muestreo de los registros es de {frec_muestreo} Hz.")
cant_datos = len(valor_parametros[:, 0])
print(f"De cada parámetro se han registrado {cant_datos} datos.")
print(f"Hay registrados un total de {cant_datos*cant_parametros} datos.")
# Pos procesamiento de registros
nuevos_datos = posprocesar.reducir_muestras(valor_parametros, frec_muestreo)
# Tiempo: se pone al tiempo inicial = 0
nuevos_datos = posprocesar.iniciar_tiempo(nuevos_datos)
# Las presiones de combustible se pasan a psia
nuevos_datos[:, 3] = nuevos_datos[:, 3]+14.7
nuevos_datos[:, 5] = nuevos_datos[:, 5]+14.7
nuevos_datos[:, 6] = nuevos_datos[:, 6]+14.7
duracion_ensayo = nuevos_datos[-1, 0]
print(f"El ensayo tuvo una duración de {duracion_ensayo:0.0f} segundos ({duracion_ensayo/3600:0.2f} horas).")
nuevo_nombre_parametros = posprocesar.renombrar_parametros(nombre_parametros)

print("\n¿Qué parámetro querés graficar:")
for nombre in enumerate(nuevo_nombre_parametros):
    print (f"{nombre[0]}: {nombre[1]}")
no_parametro = int(input("? "))
tiempo_inicial = input("Tiempo inicial: ")
tiempo_final = input("Tiempo final: ")

if tiempo_inicial == "" and tiempo_final == "":
    plt.plot(nuevos_datos[:, 0], nuevos_datos[:, no_parametro])
    plt.grid(True)
    plt.xlabel(nuevo_nombre_parametros[0])
    plt.ylabel(nuevo_nombre_parametros[no_parametro])
    plt.savefig("figura.png")
else:
    ini = int(tiempo_inicial)
    fin = int(tiempo_final)
    plt.plot(nuevos_datos[ini:fin, 0], nuevos_datos[ini:fin, no_parametro])
    plt.grid(True)
    plt.xlabel(nuevo_nombre_parametros[0])
    plt.ylabel(nuevo_nombre_parametros[no_parametro])

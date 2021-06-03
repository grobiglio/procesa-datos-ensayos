"""
Programa para lectura y procesamiento de datos de ensayos que se hallan
en un archivo .mat extraído del IADS Symvionics.
"""
# import os
import matplotlib.pyplot as plt
import ayuda
import leer
import posprocesar
import graficar

def pedir_opcion_principal():
    print("""
===============================
Menu
-------------------------------
1. Ayuda
2. Leer archivo .mat
3. Posprocesar los datos leídos
4. Graficar
5. Salir
-------------------------------
    """)
    opcion = input("Ingresar opción: ")
    return opcion

opcion = ""
while opcion != "5":
#   os.system('cls') Es para limpliar la consola
    opcion = pedir_opcion_principal()

    if opcion == "1":
        print ("Voy a ayudar")
        ayuda.ayuda()

    elif opcion == "2":
        # Lectura del archivo
        nombre_archivo = input ("Ingresar nombre de archivo: ")
        datos = leer.leer_archivo(nombre_archivo) # Diccionario
        key_valor_parametros = datos["__globals__"][0]
        key_info_parametros = datos["__globals__"][1]
        info_parametros = str(datos[key_info_parametros][0])
        frec_muestreo = leer.devolver_frecuencia_de_muestreo(info_parametros)
        nombre_parametros = leer.devolver_nombre_parametros(info_parametros)
        valor_parametros = datos[key_valor_parametros]
        print(f"Se ha leído la información del archivo {nombre_archivo}.mat.")
        cant_parametros = len(nombre_parametros)
        print(f"El archivo tiene información de {cant_parametros} parámetros.")
        print(f"La frecuencia de muestreo de los registros es de {frec_muestreo} Hz.")
        cant_datos = len(valor_parametros[:, 0])
        print(f"De cada parámetro se han registrado {cant_datos} datos.")
        print(f"Hay registrados un total de {cant_datos*cant_parametros} datos.")
        # Fin lectura de archivo

    elif opcion == "3":
        # Pos procesamiento de datos leidos
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
        # Fin pos procesamiento de datos leidos

    elif opcion == "4":
        # Gráfico de datos
        print("\n¿Qué parámetro querés graficar")
        for nombre in enumerate(nuevo_nombre_parametros):
            print (f"{nombre[0]}: {nombre[1]}")
        no_parametro = int(input("? "))
        tiempo_inicial = input("Tiempo inicial: ")
        tiempo_final = input("Tiempo final: ")

        if tiempo_inicial == "" and tiempo_final == "":
            tiempo = nuevos_datos[:, 0]
            parametro = nuevos_datos[:, no_parametro]
            unidad = ""
            graficar.una_curva(tiempo, parametro, unidad)
        else:
            ini = int(tiempo_inicial)
            fin = int(tiempo_final)
            plt.plot(nuevos_datos[ini:fin, 0], nuevos_datos[ini:fin, no_parametro])
            plt.grid(True)
            plt.xlabel(nuevo_nombre_parametros[0])
            plt.ylabel(nuevo_nombre_parametros[no_parametro])
            plt.savefig("figura.png")
        # Fin grafico de datos

    else:
        print ("Ingrese una opción entre 1 y 5.")

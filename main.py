# coding = utf-8
"""
Programa para lectura y procesamiento de datos de ensayos que se hallan
en un archivo .mat extraído del IADS Symvionics.
"""
import os
import copy
import matplotlib.pyplot as plt
import numpy as np
import leer
import posprocesar
import graficar
import preguntar
from info import info_param

os.system('cls')
figura = 0 # Inicializo el número de figura a graficar

opcion_escogida = ""
while opcion_escogida != "4":
    opcion_escogida = preguntar.pedir_opcion_principal()

    if opcion_escogida == "1":
        print("Lo siento 😥, esta oción aún no está disponible.")

    elif opcion_escogida == "2":
        # Lectura del archivo y extracción de información
        nombre_archivo = preguntar.solicitar_nombre_de_archivo()
        cont_mat = leer.leer_archivo(nombre_archivo)
        claves = leer.extraer_claves(cont_mat)
        clave_datos = claves[0]
        clave_info_export = claves[1]
        info_export = leer.extraer_info_exportacion(cont_mat,
                                                    clave_info_export)
        frec_muestreo = leer.obtener_frecuencia_de_muestreo(info_export)
        nombre_parametros = leer.obtener_nombre_parametros(info_export)
        datos = leer.extraer_datos(cont_mat, clave_datos)

        # Posprocesamiento de datos leidos
        reducir = input("¿Querés reducir la frecuencia de muestreo? (S/N): ")
        if reducir.upper() == "S":
            datos_reducidos = posprocesar.reducir_datos(datos, frec_muestreo)
            datos = np.copy(datos_reducidos)
        datos = posprocesar.iniciar_tiempo(datos)
        # Las presiones de combustible se pasan a psia
        datos[:, 3] = datos[:, 3]+14.7
        datos[:, 5] = datos[:, 5]+14.7
        datos[:, 6] = datos[:, 6]+14.7
        duracion_ensayo = datos[-1, 0]
        print(f"El ensayo tuvo una duración de {duracion_ensayo:0.0f} \
segundos ({duracion_ensayo/3600:0.2f} horas).")
        nuevo_nombre_parametros = posprocesar.renombrar_parametros(nombre_parametros)
        print("Los parámetros se renombraron. Los nuevos nombres son:")
        for nombre_parametro in nuevo_nombre_parametros:
            print(nombre_parametro)
        # Fin pos procesamiento de datos leidos

    elif opcion_escogida == "3":
        # Gráfico de datos
        id_param = {
            "no_param": 0,
            "param": ""
        }
        param_a_graficar = []
        no_parametro = -1
        print("\n¿Qué parámetro querés graficar")
        for nombre in enumerate(nuevo_nombre_parametros):
            print (f"{nombre[0]}: {nombre[1]}")
        while no_parametro != 0:
            no_parametro = int(input("? "))
            id_param["no_param"] = no_parametro
            id_param["param"] = nuevo_nombre_parametros[no_parametro]
            d = copy.deepcopy(id_param)
            param_a_graficar.append(d)
        print(param_a_graficar)
        ti = input("Tiempo inicial: ")
        tf = input("Tiempo final: ")

        if ti == "" and tf == "":
            ti = 0
            tf = duracion_ensayo
        
        tiempo = datos_reducidos[:, param_a_graficar[-1]["no_param"]]
        parametro = datos_reducidos[:, param_a_graficar[0]["no_param"]]
        unidad = ""
        graficar.graficar_varias_curvas(float(ti),
                                        float(tf),
                                        datos_reducidos,
                                        param_a_graficar,
                                        frec_muestreo,
                                        "",
                                        figura)
        figura += 1
        # Fin grafico de datos


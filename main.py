# coding = utf-8
"""
Programa para lectura y procesamiento de datos de ensayos que se hallan
en un archivo .mat extraído del IADS Symvionics.
"""
import os
import matplotlib.pyplot as plt
import leer
import posprocesar
import graficar
import copy

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
    opcion_principal = input("Ingresar opción: ")
    return opcion_principal

os.system('cls')
figura = 0

opcion_principal = ""
while opcion_principal != "5":
    opcion_principal = pedir_opcion_principal()

    if opcion_principal == "1":
        help(leer)

    elif opcion_principal == "2":
        # Lectura del archivo
        # nombre_archivo = input ("Ingresar nombre de archivo: ")
        nombre_archivo = "datos_en_bruto"
        cont_mat = leer.leer_archivo(nombre_archivo)
        print(f"Se ha leído con éxito la información del archivo {nombre_archivo}.mat.")
        key_datos = cont_mat["__globals__"][0]
        key_export_info = cont_mat["__globals__"][1]
        export_info = str(cont_mat[key_export_info][0])
        frec_muestreo = leer.devolver_frecuencia_de_muestreo(export_info)
        print(f"La frecuencia de muestreo de los registros es de {frec_muestreo} Hz.")
        nombre_parametros = leer.devolver_nombre_parametros(export_info)
        cant_parametros = len(nombre_parametros)
        datos = cont_mat[key_datos]
        print(f"El archivo tiene información de {cant_parametros} parámetros.")
        for nombre_parametro in nombre_parametros:
            print(nombre_parametro)
        cant_datos = len(datos[:, 0])
        print(f"De cada parámetro se han registrado {cant_datos} datos.")
        print(f"Hay registrados un total de {cant_datos*cant_parametros} datos.")
        # Fin lectura de archivo

    elif opcion_principal == "3":
        # Pos procesamiento de datos leidos
        nueva_frec_muestreo = int(input("Frecuencia de puestreo después de la reducción: "))
        datos_reducidos = posprocesar.reducir_datos(datos, frec_muestreo, nueva_frec_muestreo)
        # Tiempo: se pone al tiempo inicial = 0
        datos_reducidos = posprocesar.iniciar_tiempo(datos_reducidos)
        # Las presiones de combustible se pasan a psia
        datos_reducidos[:, 3] = datos_reducidos[:, 3]+14.7
        datos_reducidos[:, 5] = datos_reducidos[:, 5]+14.7
        datos_reducidos[:, 6] = datos_reducidos[:, 6]+14.7
        duracion_ensayo = datos_reducidos[-1, 0]
        print(f"El ensayo tuvo una duración de {duracion_ensayo:0.0f} segundos ({duracion_ensayo/3600:0.2f} horas).")
        nuevo_nombre_parametros = posprocesar.renombrar_parametros(nombre_parametros)
        print("Los parámetros se renombraron. Los nuevos nombres son:")
        for nombre_parametro in nuevo_nombre_parametros:
            print(nombre_parametro)
        # Fin pos procesamiento de datos leidos

    elif opcion_principal == "4":
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
                                        nueva_frec_muestreo,
                                        "",
                                        figura)
        figura += 1
        # Fin grafico de datos

    else:
        print ("Ingrese una opción entre 1 y 5.")

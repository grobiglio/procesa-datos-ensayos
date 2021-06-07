#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Este módulo tiene funciones que permite lee archivos .mat que se
obtienen del software para registro de datos de ensayos en vuelo
IADS Symvionics. Una vez leido, los datos se asignan a un diccionario
y quedan preparados para su posprocesamiento.

De la lectura se obtienen tres elementos:
    1. La frecuencia de muestreo
    2. Una lista de parámetros
    3. Un arreglo con los datos de ensayo
"""

import scipy.io


def leer_archivo(nombre_archivo: str) -> dict:
    """Lee el archivo .mat y devuelve un diccionario con el contenido
    del archivo.

    Parametros
    ----------
    nombre_archivo : str
        Nombre del archivo (sin la extensión .mat).

    Salidas
    -------
    cont_mat : dict
        Diccionario con el contenido del archivo <nombre_archivo>.mat.
    """
    print ("Leyendo el archivo...")
    nombre_archivo_con_ext = nombre_archivo + ".mat"
    cont_mat = scipy.io.loadmat(nombre_archivo_con_ext)
    return cont_mat


def devolver_frecuencia_de_muestreo(export_info: str) -> int:
    """Devuelve la frecuencia de muestreo de los datos en base a la
    información extraída del archivo .mat que se halla en info_parametros.

    Parametros
    ----------
    export_info : str
        Información de exportación que se encuentra en el archivo .mat.

    Salidas
    -------
    frec_muestreo : inf
        Frecuencia de muestreo con la que se leyeron los datos. Es la
        cantidad de datos que se registran por segundo.
    """
    frec_muestreo_tupla = str.rpartition(export_info, " ")
    frec_muestreo_str = frec_muestreo_tupla[2]
    frec_muestreo = int(frec_muestreo_str)
    return frec_muestreo


def devolver_nombre_parametros(export_info: str) -> list:
    """Devuelve una lista con los nombres de los parámetros que se hallan
    en el archivo .mat en base a las información de exportación.

    Parametros
    ----------
    export_info : str
        Información de exportación que se encuentra en el archivo .mat.

    Salidas
    -------
    nombre_parámetros : inf
        Nombre de los parámetros exportados por el sistema IADS
        Symvionics que corresponden a los datos en el archivo .mat.
    """
    nombre_parametros_tupla = str.partition(export_info, "Export info: ")
    nombre_parametros_str = nombre_parametros_tupla[2]
    nombre_parametros = nombre_parametros_str.split(", ")
    nombre_ultimo_parametro = str.partition(nombre_parametros[-1], " ( ")
    nombre_parametros[-1] = nombre_ultimo_parametro[0]
    return nombre_parametros

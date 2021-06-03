# -*- coding: utf-8 -*-
"""Lee archivos .mat para su posterior procesamiento."""

import scipy.io


def leer_archivo(nombre_archivo):
    """Lee el archivo .mat y devuelve un diccionario con la información
    contenida en el archivo.

    Parametros
    ----------
    nombre_archivo : str
        Nombre del archivo sin la extensión .mat.

    Salidas
    -------
    mat : dict
        Diccionario con la información del archivo.
    """
    print ("Leyendo el archivo...")
    nombre_archivo_con_ext = nombre_archivo + ".mat"
    mat = scipy.io.loadmat(nombre_archivo_con_ext)
    return mat


def devolver_frecuencia_de_muestreo(info_parametros):
    """Devuelve la frecuencia de muestreo de los datos en base a la
    información extraída del archivo .mat que se halla en info_parametros.
    """
    frec_muestreo_tupla = str.rpartition(info_parametros, " ")
    frec_muestreo_str = frec_muestreo_tupla[2]
    frec_muestreo = int(frec_muestreo_str)
    return frec_muestreo


def devolver_nombre_parametros(info_parametros):
    """Devuelve una lista con los nombres de los parámetros que se hallan
    en el archivo .mat en base a las información provista en info_parámetros.
    """
    nombre_parametros_tupla = str.partition(info_parametros, "Export info: ")
    nombre_parametros_str = nombre_parametros_tupla[2]
    nombre_parametros = nombre_parametros_str.split(", ")
    nombre_ultimo_parametro = str.partition(nombre_parametros[-1], " ( ")
    nombre_parametros[-1] = nombre_ultimo_parametro[0]
    return nombre_parametros

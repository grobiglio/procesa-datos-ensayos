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
import numpy as np


def leer_archivo(nombre_archivo: str) -> dict:
    """Lee el archivo .mat y devuelve un diccionario con el contenido
    del archivo.

    Parametros
    ----------
    nombre_archivo : str
        Nombre del archivo.

    Salidas
    -------
    cont_mat : dict
        Diccionario con el contenido del archivo <nombre_archivo>.mat.
    """
    try:
        print (f"Leyendo el archivo {nombre_archivo} ...")
        cont_mat = scipy.io.loadmat(nombre_archivo)
        print (f"Archivo {nombre_archivo} leido con éxito.")
        return cont_mat
    except FileNotFoundError:
        print (f"No se ha encontrado el archivo {nombre_archivo}.")
        return


def extraer_claves(cont_mat: dict) -> list:
    """Extrae las claves del contenido del archivo .mat que se hallan
    en cont_mat.

    Parametros
    ----------
    cont_mat: dict
        Diccionario con el contenido del archivo .mat.

    Salidas
    -------
    claves: list
        Lista de cadena de caracteres con las claves extraidas.
        Posición 0: Clave para leer datos
        Posición 1: Calve para leer información de exportación
    """
    clave_datos = cont_mat["__globals__"][0]
    clave_export_info = cont_mat["__globals__"][1]
    claves = [clave_datos, clave_export_info]
    return claves


def extraer_info_exportacion(cont_mat: dict, clave_info: str) -> str:
    """Extrae la información de exportación del contenido del archivo
    .mat.

    Parametros
    ----------
    cont_mat: dict
        Diccionario con el contenido del archivo .mat.
    clave_info: str
        Clave del diccionario cont_mat donde se halla la información
        de exportación

    Salidas
    -------
    info_export: str
        Información de exportación.
    """
    info_export = str(cont_mat[clave_info][0])
    print (f"Información de exportación:\n{info_export}")
    return info_export


def obtener_frecuencia_de_muestreo(info_export: str) -> int:
    """Devuelve la frecuencia de muestreo de los datos en base a la
    información extraída del archivo .mat que se halla en la
    información de exportación.

    Parametros
    ----------
    info_export : str
        Información de exportación que se encuentra en el archivo .mat.

    Salidas
    -------
    frec_muestreo : inf
        Frecuencia de muestreo con la que se leyeron los datos. Es la
        cantidad de datos que se registran por segundo.
    """
    frec_muestreo_tupla = str.rpartition(info_export, " ")
    frec_muestreo_str = frec_muestreo_tupla[2]
    frec_muestreo = int(frec_muestreo_str)
    print(f"La frecuencia de muestreo de los registros es de {frec_muestreo} \
Hz.")
    return frec_muestreo


def obtener_nombre_parametros(info_export: str) -> list:
    """Devuelve una lista con los nombres de los parámetros que se hallan
    en el archivo .mat en base a las información de exportación.

    Parametros
    ----------
    info_export : str
        Información de exportación que se encuentra en el archivo .mat.

    Salidas
    -------
    nombre_parámetros : list
        Nombre de los parámetros exportados por el sistema IADS
        Symvionics que corresponden a los datos en el archivo .mat.
    """
    nombre_parametros_tupla = str.partition(info_export, "Export info: ")
    nombre_parametros_str = nombre_parametros_tupla[2]
    nombre_parametros = nombre_parametros_str.split(", ")
    nombre_ultimo_parametro = str.partition(nombre_parametros[-1], " ( ")
    nombre_parametros[-1] = nombre_ultimo_parametro[0]
    print(f"Hay un total de {len(nombre_parametros)} parámetros.")
    print("Nombre de los parámetros que se encuentran en el archivo .mat:")
    for nombre_parametro in nombre_parametros:
        print(nombre_parametro)
    return nombre_parametros


def extraer_datos(cont_mat: dict, clave_datos: str) -> np.ndarray:
    """Extrae los datos del contenido del archivo .mat.

    Parametros
    ----------
    cont_mat: dict
        Diccionario con el contenido del archivo .mat.
    clave_datos: str
        Clave del diccionario cont_mat donde se hallan los datos
        registrados durante el ensayo.

    Salidas
    -------
    datos: np.ndarray
        Datos de ensayos.
    """
    datos = cont_mat[clave_datos]
    (cant_datos, cant_param) = np.shape(datos)
    print(f"De cada parámetro se han registrado {cant_datos} datos.")
    print(f"Hay registrados un total de {cant_datos*cant_param} datos.")
    return datos
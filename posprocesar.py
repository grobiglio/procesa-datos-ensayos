# -*- coding: utf-8 -*-
"""Pos procesa la información extraída del archivo .mat."""

import numpy as np


def reducir_muestras(datos, frec_muestreo, muestras_por_segundo=1):
    """
    Reduce la cantidad de muestras de los datos ingresados.

    Parameters
    ----------
    datos : numpy array
        Datos originales extraídos del archivo .mat.
    frec_muestreo : int
        Frecuencia de muestreo con la que se tomaron los datos que se
        encuentran en el archivo .mat.
    muestras_por_segundo : int, optional
        La cantidad de muestras por segundo que quedarán en los datos de
        salida. Valor por defecto es 1.

    Returns
    -------
    nuevos_datos : numpy array
        Los datos que quedan después de la reducción.
    """
    [filas, columnas] = np.shape(datos)
    filas_nuevos_datos = int(filas/frec_muestreo*muestras_por_segundo)
    nuevos_datos = np.zeros((filas_nuevos_datos+1, columnas))
    i = 0
    k = 0
    for row in datos:
        if i % (frec_muestreo/muestras_por_segundo) == 0:
            nuevos_datos[k, :] = datos[i, :]
            k += 1
        i += 1
    print(f"Después de la reducción quedaron {filas} datos.")
    return nuevos_datos


def iniciar_tiempo(datos):
    """
    Cambia los registros de tiempo para que inicien en cero.

    Parameters
    ----------
    datos : numpy array
        Registro de parámetros en los que la primer columna son los registros
        de tiempo.

    Returns
    -------
    datos : numpy array
        Registro de parámetros con la primer columna modificada de modo que
        el tiempo inicia en cero.

    """
    datos[:, 0] = datos[:, 0]-datos[0, 0]
    return datos


def renombrar_parametros(nombre_parametros):
    nuevos_nombres = ["Time"]
    for parametro in nombre_parametros:
        if parametro != "Time":
            nuevos_nombres.append(parametro[:-3])
    return nuevos_nombres

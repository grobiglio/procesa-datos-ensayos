# -*- coding: utf-8 -*-
"""Pos procesa la información extraída del archivo .mat.
El pos proceso abarca los siguientes pasos:
1. Reduce la cantidad de datos.
2. Cambia los registros de tiempo para que inicien en 0.
3. Cambia valores de presión para convertir presión relativa en presión
   absoluta.
"""

import numpy as np


def reducir_datos(datos: np.ndarray, frec_muestreo: int, nueva_frec_muestreo: int = 1) -> np.ndarray:
    """Reduce la cantidad de muestras de los datos ingresados.

    Parameters
    ----------
    datos : numpy.ndarray
        Datos extraídos del archivo .mat.
    frec_muestreo : int
        Frecuencia de muestreo con la que se tomaron los datos que se
        encuentran en el archivo .mat.
    nueva_frec_muestreo : int, opcional
        La cantidad de datos por segundo que quedarán en los datos de
        salida. Valor por defecto es 1.

    Returns
    -------
    datos_reducidos : numpy.ndarray
        Los datos que quedan después de la reducción.
    """
    r = frec_muestreo//nueva_frec_muestreo
    [cant_muestras, cant_param] = np.shape(datos)
    cant_muestras_reducidas = cant_muestras//r
    datos_reducidos = np.zeros([cant_muestras_reducidas, cant_param])
    for i in range(cant_muestras_reducidas):
        datos_reducidos[i, :] = datos[i*r, :]
    print(f"Después de la reducción quedaron {cant_muestras_reducidas} datos.")
    return datos_reducidos


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

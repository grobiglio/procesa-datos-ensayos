# -*- coding: utf-8 -*-
"""Pos procesa la información extraída del archivo .mat.
El pos proceso abarca los siguientes pasos:
1. Reduce la cantidad de datos.
2. Cambia los registros de tiempo para que inicien en 0.
3. Cambia valores de presión para convertir presión relativa en presión
   absoluta.
"""

import numpy as np


def reducir_datos(datos: np.ndarray, frec_muestreo: int) -> np.ndarray:
    """Reduce la cantidad de muestras de los datos ingresados.

    Parameters
    ----------
    datos : numpy.ndarray
        Datos extraídos del archivo .mat.
    frec_muestreo : int
        Frecuencia de muestreo con la que se tomaron los datos que se
        encuentran en el archivo .mat.

    Returns
    -------
    datos_reducidos : numpy.ndarray
        Los datos que quedan después de la reducción.
    """
    ingreso_del_usuario = input("Ingresar nueva frecuencia de muestreo: ")
    try:
        nueva_frec_muestreo = int(ingreso_del_usuario)
        if nueva_frec_muestreo < 1 or nueva_frec_muestreo > frec_muestreo:
            print(f"El valor ingresado sebe ser mayor o igual a 1 y menor a \
{frec_muestreo}. No se modificará la frecuencia de muestreo.")
            return datos
    except ValueError:
        print("Error en el ingreso de datos, no se modificará la frecuencia de\
 muestreo.")
        return datos
    r = frec_muestreo//nueva_frec_muestreo
    [cant_datos, cant_param] = np.shape(datos)
    cant_reducida_datos = cant_datos//r
    datos_reducidos = np.zeros([cant_reducida_datos, cant_param])
    for i in range(cant_reducida_datos):
        datos_reducidos[i, :] = datos[i*r, :]
    print(f"Después de la reducción quedaron {cant_reducida_datos} datos.")
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

import matplotlib.pyplot as plt
import numpy as np
import os

def graficar_una_curva(ti: float,
                       tf: float,
                       tiempo: np.ndarray,
                       parametro: np.ndarray,
                       frec_muestreo: int,
                       unidad: str = "",
                       figura: int = 0) -> None:
    i = round(ti*frec_muestreo)
    j = round(tf*frec_muestreo)
    nombre_figura = f"figura{figura}.png"
    plt.figure(figura)
    plt.plot(tiempo[i:j], parametro[i:j], label="Parametro")
    plt.grid(True)
    plt.xlabel("Tiempo [s]")
    plt.ylabel(unidad)
    plt.legend()
    plt.savefig(nombre_figura)
    os.system("C:/Users/Guillermo/Documents/desarrollos/procesa-datos-ensayos/"+nombre_figura)

def graficar_varias_curvas(ti: float,
                           tf: float,
                           datos: np.ndarray,
                           parametros: list,
                           frec_muestreo: int,
                           unidad: str = "",
                           figura: int = 0) -> None:
    i = round(ti*frec_muestreo)
    j = round(tf*frec_muestreo)
    nombre_figura = f"figura{figura}.png"
    plt.figure(figura)
    for parametro in parametros:
        k = parametro["no_param"]
        if k==0:
            break
        nombre = parametro["param"]
        plt.plot(datos[i:j,0], datos[i:j,k], label=nombre)
    plt.grid(True)
    plt.xlabel("Tiempo [s]")
    plt.ylabel(unidad)
    plt.legend()
    plt.savefig(nombre_figura)
    os.system("C:/Users/Guillermo/Documents/desarrollos/procesa-datos-ensayos/"+nombre_figura)

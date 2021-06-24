"""En este módulo se procesa la información que el usuario debe
ingresar.
1. Opciones del menú principal
2. El archivo que desea abrir
3. La frecuencia de muestreo después del posproceso
4. Los parámetros que quiere graficar
"""


def solicitar_opcion_principal():
    """Solicitar al usuario que ingrese una opción entre las propuestas
    en el menú principal.
    
    Parametros
    ----------
    Ninguno

    Salidas
    -------
    opcion_escogida: str
        Caracteres 1, 2, 3 o 4; dependiendo de la opción que escoga
        el usuario.
    """
    print("""
############## MENU ##############
----------------------------------
1. Ayuda
2. Leer archivo .mat y posprocesar
   la información
3. Graficar
4. Salir
----------------------------------
    """)
    opciones_validas = ["1", "2", "3", "4"]
    opcion_escogida = ""
    while opcion_escogida not in opciones_validas:
        opcion_escogida = input("Ingresar opción: ")
    return opcion_escogida


def solicitar_nombre_de_archivo():
    """Solicita que se ingrese el nombre de archivo a leer.
    
    Parametros
    ----------
    Ninguno

    Salidas
    -------
    nombre_archivo: str
        Nombre del archivo .mat a leer.
    """
    nombre_archivo = input ("Ingresar nombre de archivo (sin la extensión .mat): ")
    nombre_archivo += ".mat"
    return nombre_archivo
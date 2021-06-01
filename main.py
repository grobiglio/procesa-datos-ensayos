"""
Programa para lectura y procesamiento de datos de ensayos que se hallan en
un archivo .mat.
"""

def pedir_opcion_principal():
    print("""
    Menu
    ----
    1. Ayuda
    2. Leer archivo .mat
    3. Posprocesar los datos leídos
    4. Graficar
    5. Salir
    """)
    opcion = input("Ingresar opción: ")
    return opcion

opciones = ["1", "2", "3", "4", "5"]

opcion = ""
while opcion not in opciones:
    opcion = pedir_opcion_principal()

if opcion == "1":
    print ("Voy a ayudar")
elif opcion == "2":
    print ("Voy a leer el archivo.")
elif opcion == "3":
    print ("Voy a posprocesar los datos leidos.")
elif opcion == "4":
    print ("Voy a graficar")
else:
    print ("Voy a salir.")
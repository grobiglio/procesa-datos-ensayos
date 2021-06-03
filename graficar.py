import matplotlib.pyplot as plt

def una_curva(tiempo, parametro, unidad):
    plt.plot(tiempo, parametro)
    plt.grid(True)
    plt.xlabel("Tiempo [s]")
    plt.ylabel(unidad)
    plt.savefig("figura.png")

import matplotlib.pyplot as plt
import numpy as np

def calcular_rapidez(tiempo_total, gravedad):
    tiempo = tiempo_total  # Consideramos el tiempo total como el momento en que llega al punto más bajo
    rapidez = gravedad * tiempo

    return rapidez

def calcular_punto_mas_alto(tiempo_total, gravedad):
    tiempo_maximo = 0.0
    altura_maxima = 0.0

    tiempo = 0.0
    delta_t = 0.01  # Incremento de tiempo pequeño para mayor precisión

    while tiempo <= tiempo_total:
        altura = 0.5 * gravedad * tiempo**2

        if altura > altura_maxima:
            altura_maxima = altura
            tiempo_maximo = tiempo

        tiempo += delta_t

    return tiempo_maximo, altura_maxima

def caida_libre(tiempo_total, gravedad):
    tiempo = np.linspace(0, tiempo_total, num=100)  # Genera 100 puntos de tiempo equiespaciados
    altura = 0.5 * gravedad * tiempo**2  # Fórmula de la posición en función del tiempo

    # Encontrar el tiempo en el punto más alto (velocidad vertical = 0)
    tiempo_maximo = 0.0
    for t in tiempo:
        if 0.5 * gravedad * t**2 <= 0:
            tiempo_maximo = t
            break

    # Graficar la posición en función del tiempo
    plt.plot(tiempo, altura)
    plt.plot(tiempo_maximo, 0, 'ro', label='Punto más alto')  # Marcar el punto más alto en rojo
    plt.title("Caída libre")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Altura (m)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Solicitar al usuario los datos del problema
tiempo_total = float(input("Ingrese el tiempo total de la caída (segundos): "))
gravedad = float(input("Ingrese la aceleración debido a la gravedad (m/s^2): "))

tiempo_punto_maximo, altura_punto_maximo = calcular_punto_mas_alto(tiempo_total, gravedad)
print("El punto más alto se alcanza en t =", tiempo_punto_maximo, "segundos")
print("La altura máxima alcanzada es h =", altura_punto_maximo, "metros")

rapidez_punto_bajo = calcular_rapidez(tiempo_total, gravedad)
print("La rapidez en el punto más bajo es v =", rapidez_punto_bajo, "m/s")

# Resolver el problema de la caída libre y graficar
caida_libre(tiempo_total, gravedad)
import sys
import os

#Debido a dificultades para importar el contenido de la tarea4 hemos tenido que realizar lo siguienre para poder importarlo

# 1. Obtiene la ruta donde está este archivo (tests)
current_dir = os.path.dirname(os.path.abspath(__file__))
# 2. Obtiene la ruta de la carpeta padre (Arus MatLab)
parent_dir = os.path.dirname(current_dir)
# 3. Añade la carpeta padre al camino donde Python busca cosas
sys.path.append(parent_dir)

from src.Tarea4MarioRedondo import *

def test_kalman():
    v_real = int(input("Tenemos una velocidad real de: ")) # velocidad real 50km/h
    p = int(input("Tenemos una variación inicial de: ")) # Variación inicial
    q = float(input("Tenemos un ruido inicial de: ")) # Ruido inicial
    if probabilidad(v_real) < 0.0001:
        print("No se puede aplicar bien el filtro de Kalman, no va a ser muy fiable aplicarlo")
    else:
        k = filtro_kalman(p, q, v_real)
        t = tupla_kalman(k, v_real, p, q)
        print(f"Aplicando nuestro filtro de Kalman ({k}) obtenemos una velocidad estimada de {t[0]:.5f} y una incertidumbre de {t[1]:.5f}\n"
              f" Filtro Kalman: {k}\n Velocidad estimada: {t[0]:.5f}\n Incertidumbre obtenida: {t[1]:.5f}")
    
def test_grafica_kalman():
    #Creamos unas tuplas vacias para añadir los valores que obtendremos
    t_v_real = []
    t_v_filtrada = []
    t_v_medido = []

    #Obtenemos los datos necesarios para poder graficar
    n = int(input("Vamos a tener una iteración de: "))
    v_real = int(input("Tenemos una velocidad real de: ")) # velocidad real 50km/h
    p = int(input("Tenemos una incertidumbre inicial de: "))
    q = float(input("Tenemos un ruido inicial de: ")) # Ruido inicial
    #Iteramos n veces para poder sacar varios valores
    for i in range(n):
        
        k = filtro_kalman(p, q, v_real)
        res = tupla_kalman(k, v_real, p, q)
        #Añadimos a las tuplas sus valores para obtener los valores en cada medida
        t_v_real.append(v_real)
        t_v_filtrada.append(res[0])
        t_v_medido.append(res[2])
        #Actualizamos p debido a que varía en cada instante
        p = res[1]

    ########### Generamos el gráfico #############
    plt.figure(figsize=(10, 6))
    #1º Valores medidos por el sensor
    plt.plot(t_v_medido, 'r.', label ='Lo medido por el sensor', markersize= 12, alpha= 0.5)
    #2º Valor constante de la velocidad real
    plt.plot(t_v_real, 'k--', label ='Velocidad Real', linewidth=2)
    #3º Valor velocidad filtrada por Kalman
    plt.plot(t_v_filtrada, 'g-', label='Velocidad Filtrada', linewidth=3)

    # Etiquetas y Leyenda
    plt.title("Resultado del Filtro de Kalman")
    plt.xlabel("Tiempo")
    plt.ylabel("Velocidad")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.show() #Mostramos el gráfico

if __name__ == "__main__":
    #test_kalman()
    test_grafica_kalman()

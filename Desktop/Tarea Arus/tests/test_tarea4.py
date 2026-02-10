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

def test_Kalman():
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
    
if __name__ == "__main__":
    test_Kalman()

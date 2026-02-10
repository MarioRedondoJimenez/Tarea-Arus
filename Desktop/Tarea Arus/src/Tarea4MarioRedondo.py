import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


"""
Datos:
    v_real = 50 # velocidad real 50km/h
    p = 1 # Variación inicial
    q = 0.1 # Ruido inicial
"""

#Creamos una función a la cual le metemos una velocidad real y nos dice la probabilidad de que nuestra velocidad sea esa.
#Cuanto más alta la probabilidad mejor
def probabilidad (v_real:int):

    q_real = np.random.normal(0, 2) # Ruido con distribución normal N(0,2)
    v_media = v_real + q_real #Calculamos la velocidad media

    # Hacemos la distribución normal
    probabilidad = norm.pdf(v_media, v_real, 2) # Ponemos scale=2 pq el ruido tiene una desviación tipica de 2
    return probabilidad

# Filtro de Kalman
def filtro_kalman(variacion:int, ruido:float, v_real:int):
    
    prob = probabilidad(v_real)
    varianza = 2*2 #Como el ruido sigue una distribución normal N(0,2) nuestra desv. tipica es 2.
    p_pred = variacion + ruido #Calculamos una predicción de nuestra variación
    K = p_pred / (p_pred + varianza) #Calculamos el filtro de Kalman
    return K

#Creamos una nueva función para calcular la velocidad filtrada
def tupla_kalman(filtro:float, v_real:int, variacion:int, ruido:float):
    q_real = np.random.normal(0, 2) #Este es el ruido real q sigue una distribución N(0,2)
    v_media = v_real + q_real
    #Aplicamos el filtro y calculamos la velocidad filtrada
    v_filtrada = v_real + filtro * (v_media - v_real)
    p_pred = variacion + ruido #Calculamos una predicción de nuestra variación
    p_filtrada = (1-filtro) * p_pred #Miramos si nos podemos fiar o no de nuestro filtro
    t = [v_filtrada, p_filtrada]
    return t




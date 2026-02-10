% Tarea2MarioRedondo_Acel_vs_Tiempo.m
clc; clear; close all;

%% 1. TUS DATOS
tiempo = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 10.0, 15.0, 20.0]';
aceleracion = [0.0, 0.5, 0.7, 1.0, 1.3, 1.5, 1.7, 1.8, 1.9, 2.0, 2.0, 2.0, 1.8, 1.5, 1.2, 1.0, 0.7, 0.0, -0.5, -1.0, -2.0]';
velocidad = [0.0, 0.05, 0.12, 0.20, 0.31, 0.45, 0.61, 0.79, 0.98, 1.20, 1.43, 2.00, 2.30, 2.40, 2.50, 2.55, 2.58, 2.50, 2.00, 1.20, 0.50]';
yaw_rate = [0.0, 0.0, 0.01, 0.03, 0.04, 0.06, 0.07, 0.08, 0.10, 0.12, 0.12, 0.09, 0.07, 0.04, 0.03, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0]';
angulo_direccion = [0.0, 0.0, 2.0, 5.0, 7.0, 10.0, 12.0, 15.0, 17.0, 20.0, 20.0, 15.0, 10.0, 7.0, 5.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0]';

Ts = mean(diff(tiempo));
data = iddata(aceleracion, [velocidad, yaw_rate, angulo_direccion], Ts);

%% 2. CONFIGURACIÓN DEL MODELO (MATRIZ 3x3)
% Fila 1: Velocidad | Fila 2: Yaw Rate | Fila 3: Angulo
% Col 1: na (Salida) | Col 2: nb (Entradas) | Col 3: nk (Retardo)
Configuracion = [ 2, 2, 1; 
                  2, 2, 1; 
                  2, 2, 1 ];

% Convertimos tu matriz visual al vector que necesita MATLAB
na = Configuracion(1,1);
nb = Configuracion(:,2)'; 
nk = Configuracion(:,3)'; 
modelo = arx(data, [na nb nk]);

%% 3. SIMULACIÓN / PREDICCIÓN
% Calculamos qué aceleración predice el modelo paso a paso
prediccion = predict(modelo, data, 1);
aceleracion_estimada = prediccion.OutputData;

%% 4. GRÁFICA: ACELERACIÓN vs TIEMPO
figure('Name', 'Aceleracion vs Tiempo', 'Color', 'w');

% Dibujamos los datos REALES (Círculos azules)
plot(tiempo, aceleracion, 'bo', 'MarkerSize', 6, 'LineWidth', 1.5); 
hold on;

% Dibujamos la PREDICCIÓN DEL MODELO (Línea roja)
plot(tiempo, aceleracion_estimada, 'r-', 'LineWidth', 2); 

% Decoración de la gráfica
grid on;
xlabel('Tiempo (segundos)', 'FontSize', 12, 'FontWeight', 'bold');
ylabel('Aceleración (m/s²)', 'FontSize', 12, 'FontWeight', 'bold');
title('Evolución Temporal de la Aceleración', 'FontSize', 14);
legend('Datos Reales', 'Modelo ARX', 'Location', 'Best');

% Línea de referencia cero (para ver cuándo frena)
yline(0, 'k--', 'HandleVisibility', 'off');
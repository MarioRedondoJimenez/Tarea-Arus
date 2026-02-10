%% Tarea3-MarioRedondo

%% PARAMETROS
% Parámetros del vehículo
mass_original = 1200; % Masa original (kg)
I = 2000; % Inercia (kg*m^2)
L = 2.5; % Longitud entre ejes (m)
Cd = 0.3; % Coeficiente de arrastre
A = 2.2; % Área frontal (m^2)
g = 9.81; % Gravedad (m/s^2)

% Parámetros creados
p = mass_original * g % Peso (N)

% Parámetros de movimiento
throttle = @(t) min(1, max(0, 0.1*t)); % Aceleración
brake = @(t) 0; % Sin frenado
delta = @(t) min(pi/6, max(-pi/6, 0.1 * sin(0.1*t))); % Dirección
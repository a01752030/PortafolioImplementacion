import numpy as np
from scipy.stats import ttest_1samp, t
import matplotlib.pyplot as plt
from scipy import stats

#EJERCICIO 1

# Paso 1. Datos de las latas
pesos = [11.0,11.6,10.9,12.0,11.5,12.0,12.0,11.2,10.5,12.2,11.2,10.5,12.2,11.8,12.1,11.6,11.7,11.6,11.2,12.0,11.4,10.8,11.8,10.9,11.4]

# Paso 2. Realizar la prueba t para una muestra
t_stat, p_val = ttest_1samp(pesos, 11.7)

# Mostrar el valor t y el p-valor
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_val}")

# Paso 3. Verificar si debemos rechazar la hipótesis nula
alpha = 0.02  # 100% - 98% = 2%, dividido por 2 (prueba bilateral) = 1%. Dado que es bilateral, lo multiplicamos por 2 de nuevo.
if p_val < alpha:
    print("Rechazamos la hipótesis nula.")
else:
    print("Aplica la hipótesis nula.")

# PASO 4. CREAR GRAFICAS
# Número de grados de libertad
df = len(pesos) - 1

# Valores t críticos para alpha/2 y 1 - alpha/2
alpha = 0.02
t_crit_low = t.ppf(alpha / 2, df)
t_crit_high = t.ppf(1 - alpha / 2, df)

# Valores para trazar la distribución t
x = np.linspace(t.ppf(0.001, df), t.ppf(0.999, df), 100)
y = t.pdf(x, df)

# Graficar la distribución t
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Distribución t')

# Marcar el estadístico t y los valores críticos
plt.axvline(t_stat, color='red', linestyle='--', label='T-estadístico')
plt.axvline(t_crit_low, color='green', linestyle='--', label='T crítico bajo')
plt.axvline(t_crit_high, color='green', linestyle='--', label='T crítico alto')

plt.fill_between(x, y, where=((x < t_crit_low) | (x > t_crit_high)), color='yellow', label='Región de rechazo')

# Detalles del gráfico
plt.legend()
plt.title("Visualización del estadístico t y regla de decisión")
plt.xlabel("Valor t")
plt.ylabel("Probabilidad")
plt.grid(True)
plt.show()


print(20*"*")
#EJERCICIO 2

# Paso 1. Datos
x = np.array([17, 11, 12, 23, 20, 23, 15, 16, 23, 22, 18, 23, 25, 14, 12, 12, 20, 18, 
      12, 19, 11, 11, 20, 21, 11, 18, 14, 13, 13, 19, 16, 10, 22, 18, 23])

#Paso 2. Parametros
alpha = 0.02

#Paso 3. Cálculo del valor critico
n = len(x)
tO = stats.t.ppf(alpha/2, n-1)
print(f"t0 = {tO}")

#Paso 4. Calculo de la estadistica de prueba
m = np.mean(x)
s = np.std(x, ddof=1)
sm = s / np.sqrt(n)
te = (11.49 - m) / sm
print(f"t* = {te}")

#Paso 5. Calculo del valor p
valorp = 2 * stats.t.cdf(te, n-1)
print(f"Valor p = {valorp}")

#Paso 6. Prueba T
t_stat, p_val = stats.ttest_1samp(x, 11.7)
print(f"t statistic = {t_stat}")
print(f"p value = {p_val}")


# Por experiencias anteriores, se sabe que σ=4 minutos. Usando un nivel de significación de 0.07, ¿está justificada la tarifa adicional?

mu_0 = 11.7
sigma = 4
n = len(x)
mean_sample = np.mean(x)
z = (mean_sample - mu_0) / (sigma / np.sqrt(n))
z_critical_positive = stats.norm.ppf(1 - 0.07/2)
z_critical_negative = stats.norm.ppf(0.07/2)

print(f"z = {z}")
print(f"z_critical_positive = {z_critical_positive}")
print(f"z_critical_negative = {z_critical_negative}")

if z > z_critical_positive or z < z_critical_negative:
    print("Rechazar H0")
else:
    print("No rechazar H0")

# GRAFICAR LA NORMAL

mu_0 = 11.7
sigma = 4
n = len(x)
mean_sample = np.mean(x)

z = (mean_sample - mu_0) / (sigma / np.sqrt(n))
z_critical_positive = stats.norm.ppf(1 - 0.07/2)
z_critical_negative = stats.norm.ppf(0.07/2)


x_values = np.linspace(-4, 4, 400)
y_values = stats.norm.pdf(x_values)

plt.plot(x_values, y_values)
plt.fill_between(x_values, y_values, where=(x_values > z_critical_positive) | (x_values < z_critical_negative), color='red', alpha=0.3)
plt.axvline(z, color='green', linestyle='--', label=f'z = {z:.2f}')
plt.axvline(z_critical_positive, color='blue', linestyle='--', label=f'Z_critica_positiva = {z_critical_positive:.2f}')
plt.axvline(z_critical_negative, color='blue', linestyle='--', label=f'Z_critica_negativa = {z_critical_negative:.2f}')
plt.legend()
plt.xlabel('z')
plt.ylabel('PDF')
plt.title('Regla de decisión y estadístico de prueba')
plt.show()
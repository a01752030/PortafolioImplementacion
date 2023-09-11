import scipy.stats as stats
'''
EJERCICIO 1
'''
'''
PASO 1
Estimación por intervalo con 97% de confianza
'''
# Datos
X_bar = 4.85
sigma = 0.75
n = 20
alpha = 0.03

# Valor z para el nivel de confianza del 97%
z = stats.norm.ppf(1 - alpha/2)

# Calculando el intervalo de confianza
margin_of_error = z * (sigma / (n**0.5))
IC = (X_bar - margin_of_error, X_bar + margin_of_error)
print("Ejercicio 1")
print(10*"*")
print(IC)

'''
PASO 2
INTERVALO PARA LA SEGUNDA MUESTRA
'''

# Datos para la segunda muestra
X_bar2 = 4.56
n2 = 16

# Calculando el intervalo de confianza
margin_of_error2 = z * (sigma / (n2**0.5))
IC2 = (X_bar2 - margin_of_error2, X_bar2 + margin_of_error2)

print(IC2)
print(10*"*")

'''
¿Podemos afirmar que la porosidad del helio ha disminuido?
Si el límite superior del intervalo de confianza de cualquiera de las dos muestras es menor que 5.3, entonces podríamos decir con un 97% 
de confianza que la porosidad ha disminuido.
'''

'''
EJERCICIO 2
'''

'''
Paso 1
Tamaño de la muestra para un intervalo de confianza del 95% y ancho de 0.4
'''

# Datos
sigma = 0.75
alpha_a = 0.05
E_a = 0.4 / 2

# Valor z para el nivel de confianza del 95%
z_a = stats.norm.ppf(1 - alpha_a/2)

# Calculando el tamaño de la muestra
n_a = (z_a * sigma / E_a) ** 2
n_a = round(n_a)  # Redondeamos hacia arriba 

print("Ejercicio 2")
print(10*"*")
print(n_a)


'''
Paso 2
Tamaño de la muestra para un intervalo de confianza del 99% y ancho de 0.2:
'''
alpha_b = 0.01
E_b = 0.2 / 2

#Nivel de confianza del 99%
z_b = stats.norm.ppf(1 - alpha_b/2)

# Calculando el tamaño de la muestra
n_b = (z_b * sigma / E_b) ** 2
n_b = round(n_b)  # Redondeamos hacia arriba 

print(n_b)
print(10*"*")

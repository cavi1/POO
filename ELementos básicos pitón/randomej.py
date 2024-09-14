import random

numero_entero = random.randint(1, 10)  # Genera un número entero entre 1 y 10, inclusivo
print(numero_entero)

import random

numero_flotante = random.uniform(1.5, 5.5)  # Genera un número flotante entre 1.5 y 5.5
print(numero_flotante)

import random

colores = ['rojo', 'verde', 'azul', 'amarillo']
color_aleatorio = random.choice(colores)  # Selecciona un color aleatorio de la lista
print(color_aleatorio)

import random

numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)  # Mezcla la lista en su lugar
print(numeros)


import random

letras = ['a', 'b', 'c', 'd', 'e']
muestra_aleatoria = random.sample(letras, 3)  # Selecciona 3 elementos aleatorios
print(muestra_aleatoria)


import random

# Genera un número aleatorio con distribución normal (media = 0, desviación estándar = 1)
numero_normal = random.gauss(0, 1)
print(numero_normal)


import random

random.seed(42)  # Establece una semilla para generar los mismos números aleatorios cada vez
numero_entero = random.randint(1, 10)
print(numero_entero)


import random

numero_decimal = random.random()  # Genera un número flotante entre 0.0 y 1.0
print(numero_decimal)



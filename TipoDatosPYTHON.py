# Tipos de datos básicos en Python

# Entero (int)
numero_entero = 10
print("Entero:", numero_entero, type(numero_entero))

# Flotante (float)
numero_flotante = 3.14
print("Flotante:", numero_flotante, type(numero_flotante))

# Cadena de texto (str)
texto = "Hola, Python"
print("Cadena:", texto, type(texto))

# Booleano (bool)
es_mayor = True
print("Booleano:", es_mayor, type(es_mayor))

# Lista (list)
lista = [1, 2, 3, 4]
print("Lista:", lista, type(lista))

# Tupla (tuple)
tupla = (5, 6, 7)
print("Tupla:", tupla, type(tupla))
# No puedes hacer tupla[0] = 10  # Esto da error, la tupla es inmutable

# Diccionario (dict)
diccionario = {"nombre": "Ana", "edad": 25}
print("Diccionario:", diccionario, type(diccionario))
# Es como un objeto JSON, puedes acceder a los valores por clave

# Conjunto (set)
conjunto = {1, 2, 3}
print("Conjunto:", conjunto, type(conjunto))
# Los conjuntos no permiten duplicados

# Random sirve para generar números aleatorios
import random

print(random.randrange(1, 10))
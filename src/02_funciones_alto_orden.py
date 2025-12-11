"""
02_funciones_alto_orden.py

Uso de `lambda` junto con funciones de orden superior:
- map
- filter
- sorted
- reduce

También incluí ejemplos de funciones que reciben y devuelven funciones.
"""

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("=== Lista base ===")
print(numeros)
print()


# 1. map + lambda: aplicar una función a cada elemento
# En cálculo lambda sería como aplicar (λx. x * x) a cada número.
cuadrados = list(map(lambda x: x * x, numeros))

print("=== map + lambda (cuadrados) ===")
print(cuadrados)
print()


# 1.1 map + lambda sobre cadenas de texto
nombres = ["ana", "carlos", "beatriz"]

nombres_mayus = list(map(lambda s: s.upper(), nombres))

print("=== map + lambda (mayúsculas) ===")
print("original :", nombres)
print("MAYÚSCULAS:", nombres_mayus)
print()


# 2. filter + lambda: quedarnos solo con los números pares
# Idea en cálculo lambda: λx. x es par
pares = list(filter(lambda x: x % 2 == 0, numeros))

print("=== filter + lambda (pares) ===")
print(pares)
print()


# 2.1 filter + lambda con condición distinta (mayores a 5)
mayores_que_5 = list(filter(lambda x: x > 5, numeros))

print("=== filter + lambda (mayores que 5) ===")
print(mayores_que_5)
print()


# 3. sorted + lambda: ordenar una lista de tuplas por un criterio
personas = [
    ("Ana", 25),
    ("Carlos", 19),
    ("Beatriz", 32),
    ("Daniel", 28),
]

# Ordenar por la edad (posición 1 en la tupla)
personas_ordenadas = sorted(personas, key=lambda p: p[1])

print("=== sorted + lambda (por edad) ===")
print(personas_ordenadas)
print()


# 3.1 sorted + lambda: ordenar palabras por longitud
palabras = ["lambda", "x", "cálculo", "python"]

palabras_ordenadas = sorted(palabras, key=lambda p: len(p))

print("=== sorted + lambda (por longitud) ===")
print(palabras_ordenadas)
print()


# 4. reduce + lambda: sumar todos los elementos
# reduce recibe una función acumuladora:
#   λacc. λx. acc + x
suma_total = reduce(lambda acc, x: acc + x, numeros, 0)

print("=== reduce + lambda (suma total) ===")
print("suma_total =", suma_total)
print()


# 4.1 reduce + lambda: producto de todos los elementos
producto_total = reduce(lambda acc, x: acc * x, numeros, 1)

print("=== reduce + lambda (producto total) ===")
print("producto_total =", producto_total)
print()


# 5. Lambdas que devuelven funciones (closures)
def multiplicador(factor):
    """
    Devuelve una función que multiplica su argumento por `factor`.
    Similar a: λfactor. (λx. factor * x)
    """
    return lambda x: factor * x  # función generada dinámicamente


por_2 = multiplicador(2)
por_5 = multiplicador(5)

print("=== Lambdas que devuelven funciones (closures) ===")
print("por_2(10) =", por_2(10))  # 20
print("por_5(10) =", por_5(10))  # 50
print()


# 6. Lambdas que reciben funciones
def aplicar(funcion, valor):
    """
    Aplica una función a un valor.
    Ejemplo directo del estilo del cálculo lambda.
    """
    return funcion(valor)


print("=== Lambdas que reciben funciones ===")
print("aplicar(lambda x: x * x, 7) =", aplicar(lambda x: x * x, 7))
print("aplicar(lambda x: x - 1, 10) =", aplicar(lambda x: x - 1, 10))
print()
